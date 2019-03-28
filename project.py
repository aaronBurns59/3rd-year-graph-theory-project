# Aaron Burns
# Program Basic Description:
# A program which converts infix to postfix
# Builds NFA's from regular expressions
# Uses the single NFA's for each character to build larger NFA's
# And use that NFA to recognise any string of text

# needed for reading input from the console
import sys

# Infix => Postfix Notation 
# The reason for doing this is that Computers have an easier time reading Postfix notations of strings
# because they can do it in one left to right read
def shunt(infix):
    """Converts infix regular expressions postfix notation"""
    # stores operators as they are read in in order of precedence given by the dictionary
    # A string can be used as a stack as it is only dealing with character
    operatorStack = ''
    # stores all characters in the proper postfix notation 
    postfix = '' 
    # A dictionary that gives all the symbols into an order of precedence
    # Set up as left to right association meaning if two symbols of the same precedence meet on the stack
    # the symbol currently on the stack is popped first   
    specialSymbols ={'*':50, '+':40, '?':35,  '.':30, '|':20}

    # for loop that continues for the lenght of the string input
    for i in infix:
        # Postfix does not use brackets so they need to be explicitly dealt with
        if i  == '(':
            # appends the '(' to the stack
            operatorStack = operatorStack + i
        elif i == ')':
            # checks to see if the last item on the stack is a '('
            while operatorStack[-1] != '(':
                # adds the last symbol to the postfix string i.e. the symbol before the ')'
                # sets the stack equal to the second last charatcer of the String
                postfix, operatorStack = postfix + operatorStack[-1],  operatorStack[:-1]
            # This line deletes the '(' from the stack
            operatorStack = operatorStack[:-1]
        # handles any of the symbols that appear in the dictionary above
        elif i in specialSymbols:
            # checks if the current symbol is in the dictionary and checks the precedence of the operators in question
            # the 0 in the get is a default of the .get function
            while operatorStack and specialSymbols.get(i, 0) <= specialSymbols.get(operatorStack[-1],0):
                # adds new specials symbols read in onto the operator stack
                postfix, operatorStack = postfix + operatorStack[-1], operatorStack[:-1]
            operatorStack = operatorStack + i    
        # else handles all normal characters 1,0 a-z, A-Z 
        else:
            # Adds whatever character is read by the for loop to the postfix String 
            postfix = postfix + i
    # The while loop is used to empty the operator stack into the postfix string
    while operatorStack:
        # adds the last symbol on the operator stack to the postfix string
        postfix, operatorStack = postfix + operatorStack[-1], operatorStack[:-1]
        # sets the operator stack equal to the second last item
    return postfix

# This class is used to repsent the NFA's that will be used in this program
# NFA's are made up of states
class NFA:
    initial = None
    final = None
    # Constructor for the NFA class
    # self references the current instance of the class
    # self has to be called first and is not needed to create an instance of the class
    def __init__(self, initial, final):
        self.initial=initial
        self.final=final

# this class used to represent a state in an NFA that is used in Thompson's construction
# states in Thompson's Construction can't have more than 2 edges 
# the label just repesent the symbol that is entered e.g 1,0,a,b
class state:
    #The value None implies that you don't set the value yet
    label = None
    edge1 = None
    edge2 = None

# Creates NFAs that and appends them onto the stack
# only one nfa is returned at the end of the function as only one postfix string is passed into the function at a time
def compile(postfix):
    """Creates NFA's from the postfix Regular Expression created by the shunt function"""
    # Stack for holding NFA's
    nfaStack = []
    # for loop is used to create NFA fragments for non special characters
    for p in postfix:
        if p == '*':
            # pop only one NFA off the stack for '*' operator
            nfa = nfaStack.pop()
            # create new initial and final state
            initial, final = state(), state()
            # connect the initial state to the new initial state using edge1 and
            # connect the new initial state new final state using edge2
            initial.edge1, initial.edge2 = nfa.initial, final
            # connect the old final state to the new final state and
            # connect the new final to the new initial state
            nfa.final.edge1, nfa.final.edge2 = nfa.initial, final
            # create and push the new '*' NFA to the nfaStack using the newly made initial and final states
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)

        elif p == '+':
            # pop only one NFA off the stack for '+' operator
            nfa = nfaStack.pop()
            # create new initial and final state
            initial, final = state(), state()
            # connect the initial state to the new initial state using edge1 and
            # DO NOT CONNECT the new initial state edge2 to the new final state because the + operator does not except the empty set
            initial.edge1 = nfa.initial
            # connect the old final state to the new final state and
            # connect the new final to the new initial state
            nfa.final.edge1, nfa.final.edge2 = nfa.initial, final
            # create and push the new '*' NFA to the nfaStack
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)

        elif p == '?':
            # pop only one NFA off the stack for the '?' operator
            nfa = nfaStack.pop()
            # create new initial and final state
            initial, final = state(), state()
            # connect the new initial state to the nfa initial state
            # connect the nfa final state to the new final state
            initial.edge1, initial.edge2 = nfa.initial, final
            # connect the nfa final state to the new final state
            nfa.final.edge1 = final
            #create and push a new '?' NFA to the nfaStack
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)
            
        elif p == '.': 
            # stacks are LIFO so you pop the last item off the stack first nfa2 first than nfa1
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            # combine the two states together by setting the edge1 of the nfa1 final state to
            # the nfa2's initial state
            nfa1.final.edge1 = nfa2.initial
            # create a new NFA using the nfa1.initial and nfa2.final
                # push the new nfa onto the stack which is a concatonation of both the stack
            newNFA = NFA(nfa1.initial, nfa2.final)   
            nfaStack.append(newNFA)

        elif p == '|':
            # it doesn't matter what order the NFAs are popped off the stack for the '|' operator
            nfa2, nfa1 = nfaStack.pop(), nfaStack.pop()
            # create new initial and final
            initial, final = state(), state()
            # connect the new initial state to the initial states of nfa1 and nfa2 
            initial.edge1, initial.edge2 = nfa1.initial, nfa2.initial
            # connect the final state of nfa1 and nfa2 to the new final state
            nfa1.final.edge1, nfa2.final.edge1 = final, final
            # both NFAs now have a new initial and final state
            # create a new NFA with the initial and final state and push it to the stack
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)

        else: 
            # else is used for handling all non special symbols
            # create a new initial and final state
            initial, final = state(), state()
            # set the label of the state equal to the character entered
            # this is for later on when it needs to be compared to the characters of a sample string
            initial.label = p
            # connect the new initial state to the new final state
            initial.edge1 = final
            # edge2 is not needed for the initial state
            # create a new NFA and an push it onto the stack
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)
    # pop only one state of the stack because when it is called later only one nfa will be assigned to it
    return nfaStack.pop()

# Checks the edges of each of the states passed into this function and returns the set of states
# that are connected to the given state 
def followEdges(state):
    """Returns the set of states that can be reached from a given state following its edge arrows"""
    # create a new set with a state as its only elements
    states = set()
    states.add(state)
    # checks if the states label is a special symbol
    if state.label is None:
        # checks if edge1 is pointed to a state 
        if state.edge1 is not None:
            # if there is an edge1 follow it using the Union:|= operator
            # |= is the same as var = var + 1 in other languages
            # Recursively call the the method to check the states edge1 
            states |= followEdges(state.edge1)            
        if state.edge2 is not None:
            # if there is an edge1 follow it using the Union:|= operator
            # Recursively call the the method to check the states edge1
            states |= followEdges(state.edge2)
    return states

# shunt and compile the infix and then compare it's label to the character of the string that is given using a outer and inner for loop
# returns the final state of the NFA that was compiled using the postfix string
def match(infix, string):
    """Matches a sample output string to infix regular expressions(After they are converted to postfix)"""
    # call the shunt funciton on the infix string that is passed in
    postfix = shunt(infix)
    # call the compile function on the postfix string that was created above to create and NFA for each symbol in the postfix string
    nfa = compile(postfix)
    # a new set that only allows one copy of a state into it (as sets do)
    currentSet = set()
    # a new set to hold the next states
    nextSet = set()
    # call the followEdges method and set the currentSet of states equal to the states that the new NFAs intial state can reach
    currentSet |= followEdges(nfa.initial)
    # loop through each character of the string
    for s in string:
        # loop through the current set of states
        for c in currentSet:
            # check if the state has the same label as the character in the string 
            if c.label == s:
                # add the edge1 state to the next set including all the states that are reachable by the edge arrows
                # nextSet = nextSet + followEdges(c.edge1)
                nextSet |= followEdges(c.edge1)
        # set the currentSet equal to the nextSet
        currentSet = nextSet
        # clear the nextSet by redeclaring it
        nextSet = set()
    # check if the accept state is in the currentSet
    return (nfa.final in currentSet)

# testing that the algorithm works correctly
# print('Test for the shunting yard function')
# print(shunt('A*B+C'))
# print(shunt('A+B*C'))
# print(shunt('A*(B+C)'))
# print(shunt('A-B+C'))
# print(shunt('A|B.C'))

# TESTING ==============================================================================================
# tuple is used to store pair values for '*' operator
testTuple = [
    ('a*', ''),# pass
    ('a*', 'a'),# pass
    ('a*', 'aaaa')# pass
]
# for loop used to test data in the '*' tuple
print('Test "*" operator')
for exp, res in testTuple: 
    print(match(exp, res), exp, res)

# tuple is used to store pair values for '+' operator
testTuple = [
    ('a+a', ''),# fail
    ('a+a', 'a'),# pass
    ('a+a', 'aaaa')# pass
]
# for loop used to test data in the '+' tuple
print('Test "+" operator')
for exp, res in testTuple: 
    print(match(exp, res), exp, res)

# tuple is used to store pair values for '?' operator
testTuple = [
    ('a?', ''),# pass
    ('a?', 'a'),# pass
    ('a?', 'aaaa')# fail
]
# for loop used to test data in the '?' tuple
print('Test "?" operator')
for exp, res in testTuple: 
    print(match(exp, res), exp, res)

# tuple is used to store pair values for '|' operator
testTuple = [
    ('a|b', 'a'),# pass
    ('a|b', 'aa'),# fail
    ('a|b', 'b')# pass
]
# for loop used to test data in the '|' tuple
print('Test "|" operator')
for exp, res in testTuple: 
    print(match(exp, res), exp, res)

# tuple is used to store pair values for '.' operator
testTuple = [
    ('a.b', 'a'),# fail
    ('a.b', 'ab'),# pass
    ('a.b', 'aa')# fail
]
# for loop used to test data in the '.' tuple
print('Test "." operator')
for exp, res in testTuple: 
    print(match(exp, res), exp, res)
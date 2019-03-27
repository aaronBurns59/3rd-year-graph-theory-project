# Aaron Burns
# Program Basic Description:
# A program which converts infix to postfix
# Builds NFA's from regular expressions
# Uses the single NFA's for each character to build larger NFA's
# And use that NFA to recognise any string of text

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
    specialSymbols ={'*':50, '+':40, '-':40, '.':30, '|':20}

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

# testing that the algorithm works correctly
print(shunt('A*B+C'))
print(shunt('A+B*C'))
print(shunt('A*(B+C)'))
print(shunt('A-B+C'))
print(shunt('A|B.C'))

# This class is used to repsent the NFA's that will be used in this program
# NFA's are made up of states
class NFA:
    initial = None
    final = None

# this class used to represent a state in an NFA that is used in Thompson's construction
# States in Thompson's Construction can't have more than 2 edges 
# the label just repesent the symbol that is entered e.g 1,0,a,b
class state:
    #The value None implies that you don't set the value yet
    label = None
    edge1 = None
    edge2 = None
    
    # Constructor for the NFA class
    # self references the current instance of the class
    # self has to be called first and is not needed to create an instance of the class
    def __init__(self, initial, final):
        self.initial=initial
        self.final=final

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

        #elif p == '?':

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
            # create and push the new '*' NFA to the nfaStack using the newly made initial and final states
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
            initial.label = p
            # connect the new initial state to the new final state
            initial.edge1 = final
            # edge2 is not needed for the initial state
            # create a new NFA and an push it onto the stack
            newNFA = NFA(initial, final)
            nfaStack.append(newNFA)
        return nfaStack.pop()

def followEdges(state):
    """Returns the set of states that can be reached from a given state following its edge arrows"""
    # create a new set with a state as its only elements
    states = set()
    states.add(state)
    # checks if the states label ...........
    if state.label is None:
        #checks if edge1 is a state 
        if state.edge1 is not None:
            #if there is an edge1 follow it using the Union:|= operator
            #Recursively call the the method to check the states edge1 
            states |= followEdges(state.edge1)            
        if state.edge2 is not None:
            #if there is an edge1 follow it using the Union:|= operator
            #Recursively call the the method to check the states edge1
            states |= followEdges(state.edge2)
    return states
#Aaron Burns
#Program Basic Description:
#A program which converts infix to postfix
#Builds NFA's from regular expressions
#Uses the single NFA's for each character to build larger NFA's
#And use that NFA to recognise any string of text

#Infix => Postfix Notation 
#The reason for doing this is that Computers have an easier time reading Postifx notations of strings
#because they can do it in one left to right read

def shunt(infix): 
    #stores operators as they are read in in order of precedence given by the dictionary
    #A string can be used as a stack as it is only dealing with character
    operatorStack = ''
    #stores all characters in the proper postfix notation 
    postfix = '' 
    #A dictionary that gives all the symbols into an order of precedence 
    specialSymbols ={'*':50, '+':40, '.':30, '|':20}

    #for loop that continues for the lenght of the string input
    for i in infix:
        #Postfix does not use brackets so they need to be explicitly dealt with
        if i  == '(':
            #appends the '(' to the stack
            stack = stack + i
        elif i == ')':
            #checks to see if the last item on the stack is a '('
            while stack[-1] != '(':
                #adds the last symbol to the postfix string i.e. the symbol before the ')'
                postfix = postfix + specialSymbols[-1]
                 #sets the stack equal to the second last charatcer of the String
                specialSymbols = specialSymbols[:-1]
            #This line deletes the '(' from the stack
            specialSymbols = specialSymbols[:-1]
        elif i in specialSymbols:

        #else handles all normal characters 1,0 a-z, A-Z 
        else:

    #finished
    return postfix



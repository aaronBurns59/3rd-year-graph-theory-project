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
    #Set up as left to right association meaning if two symbols of the same precedence meet on the stack
    #the symbol currently on the stack is popped first   
    specialSymbols ={'*':50, '+':40, '-':40, '.':30, '|':20}

    #for loop that continues for the lenght of the string input
    for i in infix:
        #Postfix does not use brackets so they need to be explicitly dealt with
        if i  == '(':
            #appends the '(' to the stack
            operatorStack = operatorStack + i
        elif i == ')':
            #checks to see if the last item on the stack is a '('
            while operatorStack[-1] != '(':
                #adds the last symbol to the postfix string i.e. the symbol before the ')'
                postfix = postfix + operatorStack[-1]
                 #sets the stack equal to the second last charatcer of the String
                operatorStack = operatorStack[:-1]
            #This line deletes the '(' from the stack
            operatorStack = operatorStack[:-1]
        #handles any of the symbols that appear in the dictionary above
        elif i in specialSymbols:
            #I DONT FULLY KNOW THIS YET
            while operatorStack and specialSymbols.get(i, 0) <= specialSymbols.get(operatorStack[-1],0):
                postfix= postfix + operatorStack[-1]
                operatorStack = operatorStack[:-1]
            #adds new specials symbols read in onto the operator stack
            operatorStack = operatorStack + i    
        #else handles all normal characters 1,0 a-z, A-Z 
        else:
            #Adds whatever character is read by the for loop to the postfix String 
            postfix = postfix + i
    #The while loop is used to empty the operator stack into the postfix string
    while operatorStack:
        #adds the last symbol on the operator stack to the postfix string
        postfix = postfix + operatorStack[-1]
        #sets the operator stack equal to the second last item
        operatorStack= operatorStack[:-1]
    return postfix

#testing that the algorithm works correctly
print(shunt('A*B+C'))
print(shunt('A+B*C'))
print(shunt('A*(B+C)'))

print(shunt('A-B+C'))

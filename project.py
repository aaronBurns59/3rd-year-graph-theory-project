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
    operatorStack = ''
    #stores all characters in the proper postfix notation 
    postfix = '' 
    #A dictionary that gives all the symbols into an order of precedence 
    specialSymbols('*':50, '+':40, '.':30, '|':20)

    #for loop that continues for the lenght of the string input
    for i in infix:
        if i  == '(':
        
        elif i == ')'

        elif i in specialSymbols:

        #else handles all normal characters 1,0 a-z, A-Z 
        else

    #finished
    return postfix



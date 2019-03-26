Infix to Postfix (Shunting Yard Algorithm)
==========================================

#for this portion of the program I used strings in place of stacks because all the shunt function details with are characters

The first part of the project is to convert any regular expressions that may be entered by the user into postfix notation.
The reason for doing this is, computers have an easier time reading them than infix notation as they can process it in one left to right read. They do not have to go back over the string.

In the "shunt" function(named according to the algorithm it uses) it reads in a string parameter and returns a string  as a value. Three initial variables are created, two set to '' impling they are strings and a dictionary type that holds specials characters such as the *, ., |, and + operator. A for loop with if statements are used to handle when brackets and symbols as they are read in

The for loop continues for the lenght of the string that is passed into the functions. Inside that function if/elif/else statements are used to determine the symbol that is being read in at each position of the stack.

The if statement is entered if an opening bracket is encountered on the stack. The bracket is popped to the stack and that is all that is needed to be done so the loop iterates to the next item on the stack

The first elif is entered when the item on the stack is a closing bracket. Inside this statment a while loop checks to see if the the last item on the stack is not an opening bracket if not than whatever is on the operator stack is added to the postfix string and the stack is set equal to its second last element(essentially popping it). When all the items between the opening and closing bracket have been put into the postfix string. The opening bracket is removed from the stack and discarded

The second Elif handles any symbols that go into the operator stack that are also declared inside the dictionary. It checks using a while loop to see if the operator is in the dictionary and what precedence it has in the dictionary (* has a higher precedenc then | and .). The precedence of the operator determines if it is added to the postfix string before or after the symbol currently on the operatorStack. Some symbols have equal precedence like - and +, in that case which ever is on the operatorStack will be pushed first due to this programs lef to right association.Once the operators are added to the postfix string the operatorStack is set equal to its second last character.

The else deals with any characters that are not brackets or operators. Symbols that are just regular characters like a,b, 1 or 0. These characters aree just added to the postfix string as they enter the for loop

 At the end of the shunt function there is a while loop that empties the operatorStack in case there are any symbols left on it and it returns the postfix string that was converted from infix.


 Creating NFA's from the postfix RE (Thompson's Construction)
=============================================================

Two classes are used to represent the NFA's and the states that make up those NFA's.  The NFA class has a constructor io initialise its properties.  The state class has three variables one for the label of the state and two for the edges. The edges will be used later on the connect the states in the NFA
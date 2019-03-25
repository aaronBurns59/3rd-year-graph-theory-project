Infix to Postfix (Shunting Yard Algorithm)

The first part of the project is to convert any regular expressions that may be entered by the user into postfix notation.
The reason for doing this is, computers have an easier time reading them than infix notation as they can process it in one left to right read. They do not have to go back over the string.

In the "shunt" function(named according to the algorithm it uses) it reads in a string parameter and returns a string  as a value. Three initial variables are created, two set to '' impling they are strings and a dictionary type that holds specials characters such as the *, ., |, and + operator. A for loop with if statements are used to handle when brackets and symbols as they are read in

The for loop continues for the lenght of the string that is passed into the functions. Inside that function if/elif/else statements are used to determine the symbol that is being read in at each position of the stack.

The if statement is entered if an opening bracket is encountered on the stack. The bracket is popped to the stack and that is all that is needed to be done so the loop iterates to the next item on the stack

The first elif is entered when the item on the stack is a closing bracket. Inside this statment a while loop checks to see if the the last item on the stack is not an opening bracket if not than whatever is on the operator stack is added to the postfix string and the stack is set equal to its second last element(essentially popping it). When all the items between the opening and closing bracket have been put into the postfix string. The opening bracket is removed from the stack and discarded
 
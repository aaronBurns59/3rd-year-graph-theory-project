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


 Creating NFA's from the postfix Regular Expressions (Thompson's Construction)
==============================================================================

Two classes are used to represent the NFA's and the states that make up those NFA's.  The NFA class has a constructor io initialise its properties.  The state class has three variables one for the label of the state and two for the edges. The edges will be used later on the connect the states in the NFA

A function called compile is used to turn the postfix regular expressions created in the shunt function, into NFAs. It declares a stack for the nfas and than a series of if/elif/else statements to handle the special symbols used in 'Thompson's Construction'

The if statement is entered when the symbol in the posftix string is a '*' operator. The '*' NFA needs two new states, a new initial and final state. The new initial state needs to connect to the old initial state and the new final state. The old final state needs to connect to the new final state and the old intial state. This is done in the code by connecting the new initial state's edge1 to the old initial state and its edge2 to the new final state.  Only one NFA needs to be popped off the stack because the '*' operator in regular expressions means one or more instances are accepted.

The first elif statement is entered when the symbol in the postfix string is a '+' operator. The '+' operator is almost identical to the * operator except the new initial state is not connected to the new final state. The '+' operator NFA means one or more of an instance is accepted, removing the connection ensures that the empty set is not accepted

The second elif statement is entered when the symbol in the postfix string is a '?' operator. Pop an NFA off the stack and create an initial and final state. Connect the new initial state to the NFA's initial state and the new final state. Only connect the NFA's final state to the new final state. Do not connect it back to the NFA's initial state. This disqualifies more than one instance of a given character occuring. The '?' operator means than zero or one of an instance is accepted

The third elif statement is entered when the symbol in the postfix string is a '.' operator. The '.' operator needs two states popped off the nfaStack. Connect the nfa1's final state the the nfa2's initial state. Create a new NFA using the nfa1 initial state and the nfa2 final state. Append the new NFA onto the stack

The fourth elif statement is entered when the symbol in the postfix string is a '|' operator. The '|' operator needs two states popped off the nfaStack. It also needs a new initial and final state. Connect the new initial state to the initial states of the two NFAs that were popped off the stack And connect the two NFAs final states to the newly created final state. Create a new NFA using the newly created initial and final state. Append the new NFA onto the stack

The else statement is entered when no special characters are incountered, all non special symbols have the same NFA. Non special symbol's NFAs need a initial and a final state and nothing is popped off the stack. Non special NFAs have the state label set to whatever character is currently being read in the postfix e.g.'a', 'b', '0', '1'. The initial state's edge1 is connected to the newly created final state. A new NFA is created using the initial and final and is then appended onto the stack.

Following edges of state to determine the states that can be reached by a given state
=====================================================================================
The followEdges function take in one parameter which is of type state. The function will be used in the match function to determine and order into sets the number of states that a given state can reach by following all the edges of that state. When the function is called is declares a new set called states and adds the parameter state to the set (if the same state is passed it will not be added twice to the set). An if statement is used to check if the label is equal to None, if the label is equal to None than that current state is a special symbol becasue only non special characters are assigned to the NFA label property. It than checks to see if both edges of the state are not connected. And if they are not it adds all of the states it is connected to, to the states set(No need to worry about duplicates with sets). After the states set has been filled with the states that the given state can reach via its edges it is returned by the function

Matching sets of states NFAs to determine if they are the same
==============================================================
The match function takes in two parameters both of which are strings. One to represent an infix regular expression and another to represent a sample answer that it will be expected to either match or not. The shunt function is called on the infix string and is assigned to a new string called postfix which is then passed into the compile function which is assigned to an NFA variable. Two sets are declared one to reprsent the current states and another to represent the states that the current state is connected to via its edges. Then states that are connected to the NFAs initial state are added to the currentSet. A for loop is used to cycle through the sample string that was passed into the function and an inner for loop cycles through the currentSet. The characters of the string symbol is then compared to the label of the state in the currentSet. If the characters match than states that the current state ic connected to are added to the nextSet. After the end of the inner for loop the currentSet is set equal to the nextSet and the nextSet is reinitialised(emptied). After the sample string has been read the final NFA in the currentSet is returned, this is to check if the final state of the NFA is in the currentSet. If it is than the sample string matches the infix regular expression.



Test the shunt function
=======================
This test is very simple. it calls the shunt function and gives some sample infix regular expressions as parameters it than returns those to the console so they can be verified as postfix strings after the **shunting yard algorithm** has been used on them by the shunt function. 

Testing each operators conditions seperatly first
=================================================
The tests written for each of the operators take in as few non special characters and only one of the operators in order to test that the compile function it working properly and all the NFAs returned by it match the symbols **regular expressions**

Testing more complex RE used in graph theory
===========================================
This is very much the same as the above test except the infix REs that are given are more complex

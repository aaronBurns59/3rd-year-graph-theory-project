Infix to Postfix (Shunting Yard Algorithm)
==========================================================================================================================
The first part of the project is to convert any regular expressions that may be entered by the user into postfix notation.
The reason for doing this is, computers have an easier time reading them than infix notation as they can process it in one left to right read. They do not have to go back over the string.

In the "shunt" function(named according to the algorithm it uses) it reads in a string parameter and returns a string  as a value. Three initial variables are created, two set to '' impling they are strings and a dictionary type that holds specials characters such as the *, ., |, and + operator. A for loop with if statements are used to handle when brackets and symbols as they are read in
==========================================================================================================================
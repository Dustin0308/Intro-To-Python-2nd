# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# It prints the message in each with 'Victor' at the end. The variable 'NAME' has a value of 
# 'Victor' and even though it is in all caps, Python still recognizes it as a variable. Programmers 
# would set the variable 'name' to the value of 'Victor' to follow proper naming conventions for 
# variables. All caps is reserved for constants but that's for programmers as Python doesn't 
# recognize true constants. Same with the value for 'Nina'. It is also an example of reassignment 
# of a value for the variable 'NAME' from 'Victor' to 'Nina'. 

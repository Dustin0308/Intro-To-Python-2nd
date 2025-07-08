my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers 
# (don't write any code for this exercise):

# 1. Are the lists assigned to my_list and another_list equal? 
# Yes. They have the same values. Both are lists with the same elements.

# 2. Are the lists assigned to my_list and another_list the same object? 
# No. They are equal in value but Python recognizes them as different objects due to the list
# constructor creating a new object.

# 3. Are the nested lists at index 3 of my_list and another_list equal?
# Yes. The lists are shallow copies of each other so they are equal.

# 4. Are the nested lists at index 3 of my_list and another_list the same object?
# Yes. 'anoter_list' is a shallow copy of 'my_list'.

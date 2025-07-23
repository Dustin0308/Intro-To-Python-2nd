# Use a 'while' loop to print the numbers in 'my_list', one number per line. Then, do the same with a 
# 'for' loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected Output:
# 6
# 3
# 0
# 11
# 20
# 4
# 17

# Using a 'while' loop

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    numbers = my_list[index] 
    print(numbers)
    index += 1



# Using a 'for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]
for number in my_list:
    print(number)

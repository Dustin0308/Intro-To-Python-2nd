# Use a 'while' loop to print all numbers in 'my_list' with even values, one number per line. Then, 
# print the odd numbers using a 'for' loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected Even Values                  Expected Odd Values
# 6                                     3
# 0                                     11
# 20                                    17
# 4


# 'while' loop to print even numbers.

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    numbers = my_list[index]
    if numbers % 2 == 0:
        print(numbers)
    
    index += 1




# 'for' loop to print odd numbers.

my_list = [6, 3, 0, 11, 20, 4, 17]

for numbers in my_list:
    if numbers % 2 != 0:
        print(numbers)
    
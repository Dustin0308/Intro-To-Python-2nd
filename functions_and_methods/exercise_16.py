# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# function names: multiply, line 4 and 12, 
#                 get_num, line 7, 10, and 11,
#                 float, line 8, 
#                 input, line 8, 
#                 print, line 13

# parameters: left, line 4 and 5, 
#             right, line 4 and 5

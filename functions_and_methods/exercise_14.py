# Identify all of the identifiers on each line of the following code.

def multiply(left, right):                                  # multiply, left, right
    return left * right                                     # left, right

def get_num(prompt):                                        # get_num, prompt
    return float(input(prompt))                             # prompt, float, input

first_number = get_num('Enter the first number: ')          # first_number, get_num
second_number = get_num('Enter the second number: ')        # second_number, get_num
product = multiply(first_number, second_number)             # product, first_number, second_number, multiply
print(f'{first_number} * {second_number} = {product}')      # first_number, second_number, product, print

# Write a program that simulates a simple calculator. The program should:

# Ask the user to enter two numbers
# Ask the user to enter an operation (+, -, *, /)
# Use a 'match' statement (or 'if/elif' if using Python < 3.10) to perform the calculation
# Print the result
# Handle division by zero by printing "Error: Cannot divide by zero"




# Using 'if/elif' statements:

def calculator():
    num1 = float(input('Please enter your first number: '))
    num2 = float(input('Please enter your second number: '))
    operation = input('Please enter an operation to perform on both numbers (+, -, *, /): ')
    
    if operation == '+':
        result = num1 + num2
        print(f'{num1} {operation} {num2} = {result}')
    elif operation == '-':
        result = num1 - num2
        print(f'{num1} {operation} {num2} = {result}')
    elif operation == '*':
        result = num1 * num2
        print(f'{num1} {operation} {num2} = {result}')
    elif operation == '/':
        if num2 == 0:
            print('Error: Cannot divide by zero.')
        else:
            result = num1 / num2
            print(f'{num1} {operation} {num2} = {result}')
    else:
        print('Error: Invalid operation.')

calculator()


# Using 'match/case' statement:

def calculator():
    num1 = float(input('Please enter your first number: '))
    num2 = float(input('Please enter your second number: '))
    operation = input('Please enter an operation to perform on both numbers (+, -, *, /): ')

    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print('Error: Cannot divide by zero.')
                return
            else:
                result = num1 / num2
        case _:
            print('Error: Invalid operation.')

    print(f'{num1} {operation} {num2} = {result}')

calculator()



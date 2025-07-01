# Write a function called is_even that takes a number as a parameter and returns True if the number 
# is even, False if it's odd. Test your function with several different numbers and print the 
# results.

# Expected output: 8 is even: True
#                  7 is even: False

def is_even(number):
    if number % 2 == 0:
        return f'{number} is even: True'
    else:
        return f'{number} is even: False'
    
print(is_even(8))
print(is_even(7))
print(is_even(23))
print(is_even(12))



# Can also be done like this: 

def is_even(number):
    return number % 2 == 0

print(f'8 is even: {is_even(8)}')
print(f'7 is even: {is_even(7)}')

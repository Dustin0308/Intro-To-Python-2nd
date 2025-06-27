# Write a program named age.py that includes someone's age and then calculates and reports the 
# future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.

# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.

# This solution also appears in 'exercise_6.py'.

age = float(input('Please enter your age: '))                   # Added input, though it wasn't required.

print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')


# It can also be done like this: 

age = int(input('Please enter your age: '))                     # Added input, though it wasn't required.

print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')


# OR like this:

age = 37                                                        # This fulfills the exercise solution as asked.

print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

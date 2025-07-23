# Write a program named 'age.py' that asks the user to enter their age, then calculates and reports 
# the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years 
# old.

# age = int(input('Please enter your age: '))

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')



age = int(input('Please enter your age: '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')




# This also appears in 'exercise_2.py'.

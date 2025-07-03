# Write a program that asks the user to enter their age, then prints a message based on the 
# following conditions:

# If the age is less than 13, print 'You are a child.'
# If the age is between 13 and 17 (inclusive), print 'You are a teenager.'
# If the age is 18 or older, print 'You are an adult.'

def user_age(age):
    if age < 13:
        print('You are a child.')
    elif age <= 17:
        print('You are a teenager.')
    else:
        print('You are an adult.')

age = float(input('Please enter your age: '))
user_age(age)

# Create a program that takes a user's input for a password and checks if it meets basic security 
# requirements. The program should:

# Ask the user to enter a password
# Check if the password is at least 8 characters long
# Check if the password contains at least one digit
# Print 'Password accepted' if both conditions are met
# Print 'Password rejected' if either condition fails


def user_password(password):
    has_digit = any(char.isdigit() for char in password)
    if len(password) >= 8 and has_digit:
        print('Password accepted')
    else:
        print('Password rejected')

password = input('Please enter your password: ')
user_password(password)




# Another solution from LSBot (LSBot did say my solution above was more concise and idiomatic becasue 
# of my use of 'any()'):

def user_password(password):
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if len(password) >= 8 and has_digit:
        print('Password accepted')
    else:
        print('Password rejected')

password = input('Please enter your password: ')
user_password(password)

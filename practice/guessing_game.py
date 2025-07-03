# Guessing game with numbers

import random



def guess_number(min_num=0, max_num=100):
    random_num = random.randint(min_num, max_num) # Generate random number
    while True:
        try:
            guess = int(input('Please guess a number between 0 and 100: '))
            if guess < min_num or guess > max_num:
                print('Please enter a valid number.')
            elif guess == random_num:
                print('Correct!')
                return
            elif guess < random_num:
                print('Too low. Please try again.')
            else:
                print('Too high. Please try again.')

        except ValueError:
            print('Please enter a valid numbere between 0 and 100.')

guess_number()

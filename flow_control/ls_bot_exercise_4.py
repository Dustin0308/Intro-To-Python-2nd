# Create a program that determines letter grades based on numerical scores with the following 
# requirements:

# Ask the user to enter a numerical score (0-100)
# Use logical operators to determine the letter grade:
        # 90-100: A
        # 80-89: B
        # 70-79: C
        # 60-69: D
        # Below 60: F

# Also check if the score is valid (between 0 and 100)
# If invalid, print "Invalid score"
# Use a ternary expression to add '+' or '-' modifiers (e.g., B+ for 87, B- for 82)



def grades():
    score = int(input('Please enter a numerical score between 0 and 100: '))
    
    # Check for invalid scores first
    if score < 0 or score > 100:
        print('Invalid score.')
        return # Exit the function early
    
    if score < 60:
        print('You have received an F.')
    elif score <= 69:
        print('You have received a D-.' if score < 65 else 'You have received a D+.')
    elif score <= 79:
        print('You have received a C-.' if score < 75 else 'You have received a C+.')
    elif score <= 89:
        print('You have received a B-.' if score < 85 else 'You have received a B+.')
    else:
        print('You have received an A-.' if score < 95 else 'You have receieved an A+.')

grades()

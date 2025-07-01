# Create a function called introduce that takes two parameters: name (required) and age 
# (optional with a default value of 25). The function should print an introduction message. 
# Test it by calling it with and without the age parameter.

# Expected output: Hi, I'm Sarah and I'm 30 years old. 
#                  Hi, I'm Mike and I'm 25 years old.

def introduce(name, age=25):
    print(f'Hi, I\'m {name} and I\'m {age} years old.')

introduce('Sarah', 30)
introduce('Mike')

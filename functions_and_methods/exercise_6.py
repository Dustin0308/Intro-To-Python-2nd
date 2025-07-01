# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# Doesn't print anything because the 'return' on line 5 terminaltes the function before the call
# to print is invoked. 

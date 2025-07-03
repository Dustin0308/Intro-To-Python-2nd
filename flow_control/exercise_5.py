# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# Output will be 'Empty' since [] is falsy. On line 4, 'my_list' is also empty, so the 'else' block
# will run instead of the 'if' block.

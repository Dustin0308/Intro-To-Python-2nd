# From the 'flow control' section of the 'Intro to Programming with Python' book.

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')                 # Original code ends here
else:                                   # Added 'else' conditional for value that isn't 3.
    if value == 4:                      # Nested 'if' statement. Keep nesting to a modest 2-3 levels deep.
        print('value is 4')  
    else:
        print('value is NOT 3 or 4')
     




# Using an elif block to replace the 'else, if' on lines 7 and 8 above.

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
elif value == 4:                    # 'elif' must always come after 'if' block and before 'else' block.
    print('value is 4')
else:
    print('value is NOT 3 or 4')



# Using a 'pass' statement.

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:                    # This is done for readability purposes 
    pass # We don't care about 9    # 'pass' statement is used because block can't be empty.
else:
    print('value is something else')

# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If 
# it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the 
# argument is always an integer.

# My original solution:

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')




# Another acceptable solution:

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd') # This is a tenary expression!

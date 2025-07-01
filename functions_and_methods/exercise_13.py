# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# It will give an error. 'foo()' has 3 parameters with the second having a default value. When 
# 'foo()' is invoked, only one argument is given which fulfills the first parameter, but it stills
# requires an argument for the third parameter. Once one parameter is given a default value, the 
# parameters after it must also have a default value.

# The exact error is: 'SyntaxError: parameter without a default follows parameter with a default.'

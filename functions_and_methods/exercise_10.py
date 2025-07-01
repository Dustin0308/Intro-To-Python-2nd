# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# Will print: 42
#             3.141592
#             2

# 'foo()' is defined with 3 parameters with the second and third parameters having default values.
# Since the function was invoked and given 2 arguments, it will give the default value for the 
# third argument in the print out. 

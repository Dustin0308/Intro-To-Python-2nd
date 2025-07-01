# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# Will print: 42
#             3.141592
#             2.718
# The default values for the second and third parameters are ignored because 'foo()' was given 3
# arguments. 

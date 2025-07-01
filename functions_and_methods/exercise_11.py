# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# It will print: 42
#                3
#                2

# 'foo()' was defined with 3 parameters but only one argument was given. The second and third 
# parameters have default values, so since no argument was given for them when invoking 'foo' it 
# will print the default values for the second and third arguments. 

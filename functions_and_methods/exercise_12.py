# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# It will raise an error becasue 'foo()' requires at least one argument for the first parameter. If
# the first parameter also had a default value, it would print all 3 default values. 

# The exact error is: "TypeError: foo() missing 1 required positional argument: 'first'."

# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Will print an error because 'foo' is defined with two parameters and only one argument is given. 
# The exact error is: "TypeError: foo() missing 1 required positional argument: 'qux'."

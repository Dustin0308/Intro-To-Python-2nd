# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)


# It will raise an error because 'foo' has 2 paramaters, but 3 arguments were given. 
# The exact error is: 'TypeError: foo() takes 2 positional arguments but 3 were given.'

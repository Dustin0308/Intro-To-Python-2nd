# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# It gives an error: "NameError: name 'foo' is not defined." This gives this error because the 
# call to 'print(foo)' isn't looking to the function because there is no invocation to the function
# so 'print(foo)' looks to the global scope which does not have the name 'foo' defined anywhere.

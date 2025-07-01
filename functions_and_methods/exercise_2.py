# Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# It will print 'bar' because since there is no argument for the function 'set_foo()' given, it 
# returns 'None' which is nothing on the output. The 'print(foo)' is once again looking to the 
# global scope for 'foo' since there is no invocation of the function. When it looks to that global
# scope, it sees the variable 'foo' with a value of 'bar', which is what it prints to the output. The
# 'foo' value on line 6 shadows the 'foo' variable on line 3. 

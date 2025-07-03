# Refactor this code to use a regular if statement instead.

# def baz():
#     return ('bar' if foo() else qux())

def baz():
    if foo():
        return 'bar'
    else:
        return qux()

# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# Tuples are immutable so you can't change 'bye' to 'goodbye'. You would have to create a new tuple.

stuff = ('hello', 'world', 'goodbye', 'now')


# OR this way but this still creates an entirely new tuple. 

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# Don't worry about having an exact match for the output. The important part is to show something 
# that accurately represents 'set2.'

# {42, 'Monty Python', ('a', 'b', 'b'), range(5, 10)} because 'set1' and 'set2' are both 
# referencing the same object in memory. So when you add 'range(5, 10)' to 'set1', since 'set2'
# is 'set1', the changes will reflect in 'set2' as well.

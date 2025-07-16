# Which of the following values can't be used as a key in a dict object, and why?

'cat'                               # Can be used. 
(3, 1, 4, 1, 5, 9, 2)               # Can be used. 
['a', 'b']                          # Can't be used because lists are mutable. 
{'a': 1, 'b': 2}                    # Can't be used because dictionaries are mutable. 
range(5)                            # Can be used.           
{1, 4, 9, 16, 25}                   # Can't be used because sets are mutable.
3                                   # Can be used. 
0.0                                 # Can be used.
frozenset({1, 4, 9, 16, 25})        # Can be used.

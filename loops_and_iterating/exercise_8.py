# Write a comprehension that creates a dict object whose keys are strings and whose values are the 
# length of the corresponding key. Only keys with odd lengths should be in the dict. 
# Use the set given by 'my_set' as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0 }
print(result)                       # {'Cocoa': 5, 'Pudding': 7, 'Cheddar': 7}

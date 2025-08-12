# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# [1, 42, 3] because even though the dicts are different objects, they share value components since
# the 'dict' constructor creates a shallow copy. So mutations to 'dict1' would reflect in 'dict2'. 

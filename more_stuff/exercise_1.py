# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# The code prints: CHRIS

# It first calls 'dictionary.keys' to get a dictionary view of all the keys for the 'dictionary'
# object.

# Composition is then used to call 'sorted' on the dicitonary view to get a sorted list of the keys
# in the 'dictionary' object. This sorted list is: 
# ['Anotonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor'] 

# Method chainging is then used to get the sorted 'dictionary' key at index poistion 1.

# Finally, the 'upper' method is called on the key at index position 1.

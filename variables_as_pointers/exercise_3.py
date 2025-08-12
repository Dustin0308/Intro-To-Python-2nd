# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# 'The Life of Brian'. Since 'dict2' creates a nested list, the change to 'dict2' on line 10 above
# wouldn't reflect in 'dict1'.

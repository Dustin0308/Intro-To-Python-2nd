# Using a 'while' loop.


names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']




# Using a 'for' loops.

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']



# Suppose we want all the uppercase names in our upper_names list except 'Max'. The continue 
# statement can help us do that.

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue                            # 'continue' causes the loop to skip or ignore and jump to the next iteration. 

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']



# Rewriting a loop that uses 'continue' with a negated 'if' conditional:

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name != 'Max':
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']

# Write a function called 'increment_counter' that increments a counter variable every time it is 
# called. You can test your code with the following:


counter = 0                 # Added lines 5-9

def increment_counter():    
    global counter
    counter += 1


print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

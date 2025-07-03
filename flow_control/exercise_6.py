# Write a function that takes a string as an argument and returns an all-caps version of the string 
# when the string is longer than 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(my_string):
    if len(my_string) > 10:
        return my_string.upper()
    else:
        return my_string

print(all_caps('hello world'))
print(all_caps('goodbye'))

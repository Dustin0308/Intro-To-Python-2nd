# Explain why the code below prints different values on lines 3 and 4 (lines 5 and 6 for me).

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8           # This takes a slice of the string before using 'rfind' so that specific index [21:35] is all that is searched, not the whole string.
print(text.rfind('f', 21, 35))    # 29          # This takes the whole string starting at index [0] and then searches for 'f' from the right within the postition defined within that whole string.

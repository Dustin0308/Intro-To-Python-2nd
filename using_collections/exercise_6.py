# What will the following code print?

print('abc-def'.isalpha())              # False. '-' is not a letter.
print('abc_def'.isalpha())              # False. '_' is not a letter.
print('abc def'.isalpha())              # False. space is not a letter.
print('abc def'.isalpha() and           # False. Will run code and stop at 'isalpha'.
      'abc def'.isspace())
print('abc def'.isalpha() or            # False. Both are false. 
      'abc def'.isspace())
print('abcdef'.isalpha())               # True. All are letters.
print('31415'.isdigit())                # True. All numbers.
print('-31415'.isdigit())               # False. '-' is not a number.
print('31_415'.isdigit())               # False. '_' is not a number.
print('3.1415'.isdigit())               # False. '.' is not a number.
print(''.isspace())                     # False. String is empty.

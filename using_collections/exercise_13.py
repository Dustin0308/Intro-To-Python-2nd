# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)               # True
print('Butter' in cats)                     # False. Strings must match exactly.
print('Butter' in cats[3])                  # True. 'Butter' is in 'Butterscotch'. 
print('cheddar' in cats)                    # False. 'c' != 'C'.

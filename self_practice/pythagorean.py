# a² + b² = c²
import math

leg_1 = float(input('Please input A: '))
leg_2 = float(input('Please input B: '))
result = math.sqrt((leg_1)**2 + (leg_2)**2)
print(f'{result} is the length of your hypotenuse.')

# Using a function

def hypotenuse(leg_1, leg_2):
    return math.sqrt(((leg_1)**2 + (leg_2**2)))

print(f'This is the length of your hypotenuse: ', (hypotenuse(3, 4)))

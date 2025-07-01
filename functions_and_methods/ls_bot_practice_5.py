# Create a function called find_extremes that takes three numbers as parameters and returns both 
# the minimum and maximum values using the built-in min and max functions. The function should 
# return a string that describes both values.

# Expected output:
 
# Among 5, 12, and 8: minimum is 5, maximum is 12
# Among -3, 7, and 2: minimum is -3, maximum is 7

def find_extremes(num1, num2, num3):
    return min(num1, num2, num3), max(num1, num2, num3)


print(f'Among 5, 12, and 8: minimum is {min(find_extremes(5, 12, 8))}, max is {max(find_extremes(5, 12, 8))}')
print(f'Among -3, 7, and 2: minimum is {min(find_extremes(-3, 7, 2))}, max is {max(find_extremes(-3, 7, 2))}')



# Here is a better approach: 

def find_extremes(num1, num2, num3):
    minimum = min(num1, num2, num3)
    maximum = max(num1, num2, num3)
    return f'minimum is {minimum}, maximum is {maximum}'

print(f'Among 5, 12, and 8: {find_extremes(5, 12, 8)}')
print(f'Among -3, 7, and 2: {find_extremes(-3, 7, 12)}')

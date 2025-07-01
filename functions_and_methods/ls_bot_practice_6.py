# Write a function called temperature_stats that takes three temperature readings (in Fahrenheit) 
# as parameters and returns a formatted string showing the coldest temperature, the warmest 
# temperature, and the average temperature. Use the built-in min, max, and sum functions in your 
# solution.

# Expected output: 

# Temperatures 68, 72, and 75: coldest is 68°F, warmest is 75°F, average is 71.66666666666667°F
# Temperatures 32, 45, and 38: coldest is 32°F, warmest is 45°F, average is 38.333333333333336°F


def temperature_stats(temp1, temp2, temp3):
    temperatures = (temp1, temp2, temp3)
    coldest = float(min(temperatures))
    warmest = float(max(temperatures))
    average = float(sum(temperatures) / 3)
    return f'coldest is {coldest}°F, warmest is {warmest}°F, average is {average}°F'

print(f'Temperatures 68, 72, and 75: {temperature_stats(68, 72, 75)}')
print(f'Temperatures 32, 45, and 38: {temperature_stats(32, 45, 38)}')

# OR

def temperature_stats(temp1, temp2, temp3):
    temperatures = (temp1, temp2, temp3)
    coldest = min(temperatures)
    warmest = max(temperatures)
    average = sum(temperatures) / 3
    return f'Temperatures {temp1}, {temp2}, and {temp3}: coldest is {coldest}°F, warmest is {warmest}°F, average is {average}°F'

print(temperature_stats(68, 72, 75))
print(temperature_stats(32, 45, 38))

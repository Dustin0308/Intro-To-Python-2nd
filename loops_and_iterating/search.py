numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break   # Tells Python to terminate the nearest enclosing loop once we find the desired element.

    index += 1

print(found_item)

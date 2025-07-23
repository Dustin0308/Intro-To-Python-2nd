# Print all of the even numbers in the following list of nested lists. Don't use any 'while' loops.

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# Expected Output
# 6
# 4
# 2
# 4
# 16
# 0

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)














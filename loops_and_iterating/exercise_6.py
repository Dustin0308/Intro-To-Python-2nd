# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of 'my_list'. In this problem, you should 
# write code that creates a new list with one element for each number in 'my_list'. If the original 
# number is an even, then the corresponding element in the new list should contain the string 
# 'even'; otherwise, the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# Expected Output: 

# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]


# This was my solution using a ternary expression:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]


new_list = [ 'even' if number % 2 == 0 else 'odd' for number in my_list ]
print(new_list)
        

# Launch School had these solutions:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)


# And this: 

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]
print(result)


# All 3 solutions provide the same results. Some are cleaner than others though. 

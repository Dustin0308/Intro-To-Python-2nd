# Write Python code to create a new tuple from '(1, 2, 3, 4, 5)'. The new tuple should be in reverse 
# order from the original. It should also exclude the first and last members of the original. The 
# result should be the tuple '(4, 3, 2)'.

my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reversed(my_tuple[1:4])
print(tuple(reversed_tuple))                # (4, 3, 2)


# Please note: This solution was not shown in the Launch School book. I varified with LSBot
# that it is still a 'perfectly valid and correct wat to solve the problem.'

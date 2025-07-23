# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# It is an infinite loop because the code block must modify counter somehow. 'counter += 1' would do
# the trick. 

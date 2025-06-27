# Repeat the previous question but, this time, use augmented assignment to compute the final result, 
# one year at a time.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% 
# (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have 
# $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create 
# a variable named balance that contains the amount of money you will have after 5 years, then print 
# the result. 

balance = 1000
balance *= 1.05     # After 1 year
balance *= 1.05     # After 2 years
balance *= 1.05     # After 3 years
balance *= 1.05     # After 4 years
balance *= 1.05     # After 5 years.
print(balance)      # 1276.2815625000003

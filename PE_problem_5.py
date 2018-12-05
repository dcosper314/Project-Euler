#Problem 5: What is the smallest number that is divisible by all
#of the numbers 1 to 20
#Answer: 232792560

from math import gcd

n = 1
#the variable n will contain our factors. It will run from
#1 to 20

m = 1
#This variable will be updated to get our least common multiple 

while n < 21:
	if m % n == 0:
		n = n + 1
	else:
		g = gcd(m,n)
		k = n // g
		m = m*k
		n = n + 1
#basically if m is not a multiple of n, then we update m
# with the missing common factors to make m % n == 0

print(m)

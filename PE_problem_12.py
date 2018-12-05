#Problem 12: A triangular number is of the form 
#1 + 2 + ... + n.  What is the value of the first 
#triangular number to have over 500 divisors?
#Answer: the 12375th triangular number, which is 76576500

import math
def trinum(n):
	k = 0
	for i in range(1,n+1):
		k = k + i
	return k
		
#This calculates the nth triangular number

def trinumfac(n):
	k = trinum(n)
	lst = []
	for i in range(1,math.floor(k**0.5)+1):
		if k % i == 0:
			lst = lst + [i] + [k/i]
	return lst
	
#This compiles a list offactors of the nth triangular number

x = 1

while len(trinumfac(x)) < 501:
 	x = x + 1
print(x)
print(trinum(x))


#how it works: basically we compile lists of factors of nth
#trinum and stops when the length is 500. There may be more than
#one triangular number with 500 factors, but this will give the first.

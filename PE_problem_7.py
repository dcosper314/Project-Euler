# Problem 7: What is the 10,001st prime number?
# Answer: 104,743

from math import gcd
prime = [2]
#list of primes

n = 3
#n will be the integers we loop through and check 

m = 2
#m carries info about the list prime. Basically, m will always
#be the product of all elements of the list prime.

while len(prime) < 10002:
	if gcd(m,n) == 1:
		prime = prime + [n]
		m = m * n
		n = n + 1
	else:
		n = n + 1

print(prime[10000])

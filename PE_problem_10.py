#Find the sum of all primes below two million.
#The trick here is finding an efficient method for finding the primes.
#This is achieved using the sieve of Eratosthenes.

#SOLUTION:

def sumofprimes(n):
	#This first bit forms an array of True values. Then
	#starting from 2, the loop will run through the array and 
	#change every 2*k entry in the array to False (because they 
	#are not prime. Then it finds the next True value and repeats.
	sieve = [True for i in range(n+1)]
	p = 2
	while p*p<= n:
		#Note: We only need to run p through integers less than 
		#sqrt of n. This is a number theoretic idea.
		if sieve[p] == True:
			for i in range(p*2,n+1,p):
				sieve[i] = False
		p = p + 1
	#Now we sum over the indices of true values in the array.
	sum = 0
	for k in range(2,n+1):
		if sieve[k] == True:
			sum = sum + k
	return sum
print(sumofprimes(2000000))		

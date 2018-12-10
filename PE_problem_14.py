# The Collatz problem is a classic number theory problem. If given
# a starting integer, we apply the mapping:
#n -- > n/2, if n is even
#n -- > 3n+1, if n is odd
# If the result after applying the map is 1, stop. If not, apply
# the map to the resulting integer. Continue until you get 1.
# For example 3-->10-->5-->16-->8-->4-->2-->1

#Which integers below 1000000 generate the longest mapping chain?
#SOLUTION:

def collatz_map(n):
	#This is the literal mapping described in the comments.
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n + 1
	return n

def collatz_chain(n):
	#This will iteratively map n using Collatz map until we reach 1
	# and will list all integers in the chain which are below n.
	chain = [n]
	while n != 1:
		n = collatz_map(n)
		if collatz_map(n) > n:
			chain = chain
		else:
			chain = chain + [n]
	return chain

def collatz_chain_length(n):
	#this is a more efficient way to calculate chain length
	#which does not use lists
	steps = 1
	while n != 1:
		n = collatz_map(n)
		steps = steps + 1
	return steps

def c_sieve(n):
	#This is the collatz sieve. This saves a lot of time, as
	#we do not make too many redundant calculations.
	sieve = [True for i in range(n+1)]
	
	#These length and index variables represent the index
	#with the longest collatz chain and its length, which will
	#be updated as we find longer chains.
	length = 1
	index = 1
	p = n
	#Note: we start at n and work down, so as to eliminate
	#even more redundant computations.
	while p > 1:
		if sieve[p] == True:
			k = int(p)
			if collatz_chain_length(k) > length:
				length = collatz_chain_length(k)
				index = k
			if k <= n:
				while k < n + 1 and sieve[k] == True:
					sieve[k] = False
					k = int(collatz_map(k))
			elif k > n:
				k = int(collatz_map(k))
			p = p - 1
		else:
			p = p - 1
	return(index,length)
print(c_sieve(1000000))


#You may wish to compare the efficiency of this to a brute force method.
#Running the code below will take several (more than 15) minutes to finish.
lst = []
for i in range(1,1000001):
	lst = lst + [collatz_chain_length(i)]
print(max(lst))	

#Answer: index 837799 has the longest chain, with length 525

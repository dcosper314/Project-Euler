#Problem 4: Find the largest palindrome number
#made from the product of two 3-digit numbers.
#Note: Example of palindrome: 9009
#Answer: 906609

n = 999
m = 999
#We use m,n to represent the 3-digit numbers we
#multiply. We start at 999 because we want 'large'
#numbers.

while n > 99:
	while m > 99:
		y = str(m*n)
		z = y[::-1]
		#y[::-1] writes the string backwards
		
		if z == y and m*n > 900000:
			print(z)
		m = m - 1
	n = n - 1
	m = 999
#We have to run through all of the m's for every
#n value we want to check 

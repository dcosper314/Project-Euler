#Problem 6: Find the difference between the sum of squares
#of the first one hundred natural numbers and the square of
#the sum. Ex: (1+2+3)^2 - (1^2+2^2+3^2)
#Answer: 25164150

#the first part is to square the sums
a = 1
b = 0

while a < 101:
	b = b + a
	a = a + 1
	x = b**2
print(x)

#the second part is to sum the squares
n = 1
m = 0

while n < 101:
	m = m + n**2
	n = n + 1
	y = m
print(y)

print(x - y)

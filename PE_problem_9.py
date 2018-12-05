#Problem 9: There exists exactly one Pythagorean
#triplet for which a+b+c=1000.  Find the product
#a*b*c.
#Answer: [200,375,425], 31875000

a = 1
b = 1
c = 1000 - a - b

while a < 500:
	while b < c:
		if a**2 + b**2 == c**2:
			print([a,b,c])
			print(a*b*c)
			b = b + 1
		
		else: b = b + 1
		c = 1000 - a - b
	a = a + 1
	b = a

#Problem 3: What is the largest prime factor
#of 600851475143?
#Answer: 6857

given = 600851475143
integer = 2

while integer < given:
	if given % integer == 0:
		given = given/integer
	else:
		given = given
	integer = integer + 1

print(given)
#Once you find a factor of given, then we may divide
#it out of the given and find the next factor in
#a smaller number.

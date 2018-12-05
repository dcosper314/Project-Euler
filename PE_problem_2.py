#Problem 2: By considering the terms in the Fibonacci
#sequence which do not exceed four million, find the
#sum of the even valued terms.
#Answer: 4,613,732

x1 = 1
x2 = 2
x3 = 3

#These three variables will carry three consecutive
#Fibonacci terms.

even_sum = 0

while x3 < 4000000:
	if x3 % 2 == 0:
		even_sum = even_sum + x3
	else: even_sum = even_sum
	x1 = x2
	x2 = x3
	x3 = x1 + x2

print(even_sum + 2)
#We must add 2 because x_3 started at 3

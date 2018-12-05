#Problem 1: Find the sum of all multiples of 3 or 5
# below 1000.
# Answer: 233,168

sum3 = 0
for n in range(3,1000,3):
	sum3 = sum3 + n

sum5 = 0
for n in range(5,1000,5):
	sum5 = sum5 + n


sum15 = 0
for n in range(15,1000,15):
	sum15 = sum15 + n

print(sum3 + sum5 - sum15)
#you must subtract the sum of multiples of 15 
#because when you add sum3 and sum5, you add 
#some numbers twice.

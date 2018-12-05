#Find the sum of the digits of the number 100!

#SOLUTION:
import math
#We're going to be using the factorial method which is in math module.

#Similar to Problem 16, we write the factorial as a string
factorial_string = str(math.factorial(100))

#split will not work on the factorial string since there is no
#whitespace, so we form a list instead.
digit_list = [int(i) for i in factorial_string]

#the code below will add the digits from the list of digits
digit_sum = 0
for i in digit_list:
	digit_sum = digit_sum + i
print(digit_sum)

#Answer: 648

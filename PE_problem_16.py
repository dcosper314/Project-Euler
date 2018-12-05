#What is the sum of the digits of the number 2**1000?

#SOLUTION:	
#Since we want to consider the digits, it might be helpful to
#write 2**1000 as a string.
power_string = str(2**1000)

#split won't work here because there is no whitespace
#but we can form a list "by hand"
digit_list = [int(i) for i in power_string]

#This will sum the digits in digit_list
digit_sum = 0
for i in digit_list:
	digit_sum = digit_sum + i
	
print(digit_sum)

#Soltuion = 1366

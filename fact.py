num = input("Enter the factorial num:")
num1 = num
while num > 0:
	fact = num1 * (num - 1)
	num -= 1
	num1 = fact 
        if num == 1:
		print "The Factorial of given num  is:", fact		


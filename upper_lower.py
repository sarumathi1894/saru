def uplowe(string):
	lower = 0
	upper = 0
	space = 0
	for i in string:
		if ( i.islower() == True):
			lower = lower + 1
		elif (i.isupper() == True):
			upper = upper + 1
		else:
			space = space + 1
			
	print "Lower case:", lower
	print "Upper case:", upper
string = raw_input("Enter the String:")
uplowe(string);



a = raw_input("Enter the armstrong value:")
length = len(a)
num = 0
for i in a:
	arm = int(i) ** length + num
	num =  arm
if (arm == int(a)):
	print "The given num is armstrong num:", arm
else:
	print "the given num is not armstrong num"
		

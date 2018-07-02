a = input("Enter the value:") 
lt = []
lt1 = []
for i in range(1,a+1):
	if (i % 2 == 0):
		lt.append(i)
	else:
		lt1.append(i)
ct = len(lt)
ct1 = len(lt1)		 
print "The number of even num present in range is ", ct
print "The number of odd num in the range is", ct1

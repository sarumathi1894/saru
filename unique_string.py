
def list1(l1):
	print "Given list", l1
	l2 = []
	for i in l1:
		if i not in l2:
			l2.append(i)
	print "Unique list", l2	

list1([1,2,3,3,3,3,4,5]);



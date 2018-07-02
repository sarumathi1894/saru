def palindrome(a):
	if (a == a[::-1]):
		print "the given string is palindrome"
	else:
		print "nope"
a = raw_input("Enter the string:")
palindrome(a);

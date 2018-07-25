import re
file_open = open("dummy.txt","r")
file_op = open("f2.txt","w")
#print file_open.read()
#str_change = raw_input("Enter the string to change:")
str_find = raw_input("Enter the string to find:")
change = str_find[::-1]
for line in file_open:
        b = line.replace(str_find,change)
 #       print b
	file_op.write(b)



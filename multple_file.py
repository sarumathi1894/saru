import re
file_open = open("file.txt","r+")
file_op = open("f3.txt","w")
#print file_open.read()
str_change = raw_input("Enter the string to change:")
str_find = raw_input("Enter the string to find:")
for line in file_open:
	b = line.replace(str_find,str_change)
	file_op.write(b)

file_open.close()
file_op.close()

	
		
		
	
	



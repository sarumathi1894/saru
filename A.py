def A():
	for row in range(0,7):
		for col in range(0,5):
			if  ((col == 0 or col == 4 ) and row != 0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
				print "*",
			else:
				print " ",
		print
#*********J********
def J():
	for row in range(0,7):
        	for col in range(0,5):
                	if (row == 0) or (col == 2) or (row == 6 and col < 3):
                        	print "*",
                	else:
                        	print " ",
        	print

# ****************G**************
def G():
	for row in range(0,7):
        	for col in range(0,6):
                	if (col == 0) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or (row == 3 and col > 2) or (col == 4 and row > 2) or (col == 4 and row == 0):
                        	print "*",
                	else:
                        	print " ",
        	print

#***********J*****************
def J():
	for row in range(0,7):
        	for col in range(0,5):
                	if (row == 0) or (col == 2) or (row == 6 and col < 3):
                        	print "*",
                	else:
                        	print " ",
        	print

#**********K**************
def K():
	for row in range(0,7):
        	for col in range(0,5):
                	if (col == 0) or (row == 0 and col == 4) or (row == 1 and col == 3) or (row == 2 and col == 2) or (row == 3 and col == 1) or (row == col + 2 and col > 1):
                        	print "*",
                	else:
                        	print " ",
        	print
            
#**************M****************
def M():
	for row in range(0,7):
        	for col in range(0,7):
                	if (col == 0) or (col == 6) or (row == col and row < 4) or (row == 2 and col == 4) or (row == 1 and col == 5):
                        	print "*",
                	else:
                        	print " ",
        	print



#***************N************
def N():
	for row in range(0,7):
        	for col in range(0,7):
                	if (col == 0) or (col == 6) or (row == col):
                        	print "*",
                	else:
                        	print " ",
       		print

#**********Q*******************
def Q():
	for row in range(0,8):
        	for col in range(0,5):
                	if ((col == 0 or col == 4) and ( row > 0 and row < 6)) or ( (row == 0 or row == 6) and (col > 0 and col < 4)) or (row == 5 and col == 1) or ( row == 7 and col == 3) :
                        	print "*",

                	else:
                        	print " ",
        	print

#*********R******************
def R():
	i = 3
	j = 1
	for row in range(0,6):
        	for col in range(0,4):
                	if (col == 0) or ( row < 3 and col == 3) or ( (row == 0 or row == 2) and (col < 3)):
                        	print "*",
               		elif (row == i and col == j):
                        	print "*",
                        	i += 1
                        	j += 1
                	else:
                        	print " ",
        	print


#*****************V*************
def V():
	i = 0
	j = 6
	for row in range(0,4):
        	for col in range(0,7):

                	if (row == i and col == j):
                        	print "*"
                        	i += 1
                        	j -= 1
                	elif (row == col):
                        	print "*",
                	else:
                        	print " ",
        	print

#*************W****************

def W():
	i = 0
	j = 3
	for row in range(0,4):
        	for col in range(0,7):
                	if col == 0 or col == 6 or (row == 1 and col == 2) or (row == 2 and col == 1):
                        	print "*",
                	elif (row == i and col == j):
                        	print "*",
                        	i += 1
                        	j += 1
                	else:
                        	print " ",
        	print




#*************X*****************
def X():
	i = 0
	j = 4
	for row in range(0,5):
        	for col in range(0,5):
			if ( row == i and col == j):
                        	print "*",
                        	i += 1
                        	j -= 1
                	elif ( row == col):
                        	print "*",
                	else:
                        	print " ",
        	print

#**********Y****************
def Y():
	for row in range(0,5):
        	for col in range(0,5):
                	if (row > 1 and col == 2) or ( row == col and col < 3) or (row == 0 and col == 4) or (row == 1 and col == 3)  :
                        	print "*",
                	else:
                        	print " ",
        	print

#**********Z***************
def Z():
	i = 1
	j = 4
	for row in range(0,6):
        	for col in range(0,6):
                	if (row == 0) or (row == 5):
                        	print "*",
                	elif (row == i and col == j):
                        	print "*",
                        	i += 1
                        	j -= 1
                	else:
                        	print " ",
        	print

                      
string = raw_input("Enter the String:")

for i in string.upper():
	if i  == 'A':
		A();
	elif i == 'G':
		G();
	elif i == 'J':
		J();
	elif i == 'K':
		K();
	elif i == 'M':
		M();
	elif i == 'N':
		N();
	elif i == 'Q':
		Q();
	elif i == 'R':
		R();
	elif i == 'V':
		V();
	elif i == 'W':
		W();
	elif i == 'X':
		X();
	elif i == 'Y':
		Y();
	elif i == 'Z':
		Z();
	
	else:
		print i


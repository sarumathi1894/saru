fo = open("file.txt","ab+")
lines = 0
words = 0
charac = 0
fo.write("Python is a great language.");
for line in fo:
	words_split = line.split()
	print words_split
	words = words + len(words_split)
	lines = lines + 1
	charac = charac + len(line)
print words
print lines
print charac
fo.close()

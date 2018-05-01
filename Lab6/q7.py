string = raw_input("enter string ")
l = 0
d = 0
count = 0
print string
while(count < len(string)):
	if(string[count].isalpha()):
		l = l+1
		count = count + 1
	elif(string[count].isdigit()):
		d = d+1
		count = count + 1
	else:
		count = count + 1
print "Letters ", l  , "|   Digits " , d

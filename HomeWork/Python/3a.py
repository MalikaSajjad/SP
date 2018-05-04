def fix_start(st):
	lst = []
	lst.append(st[0])
	#print type(lst)
	st = st[1:]
	for ch in st:
		if ch == lst[0]:
			lst.append('*')
		else:
			lst.append(ch)
	st = ''
	for ch in lst:
		st = st + ch
	return st 

print "input: babble \noutput: ", fix_start("babble")

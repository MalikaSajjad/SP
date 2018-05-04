def fix_me(st,ch):
	index = 0
	if ch in st:
		for indx, val in enumerate(st):
			if ch == val:
				index = indx
				break
	lst = []
	i = 0
	while i <= index:
		lst.append(st[i])
		i = i + 1
		
	st = st[index + 1:]
	for ch in st:
		if ch == lst[index]:
			lst.append('*')
		else:
			lst.append(ch)
	st = ''
	for ch in lst:
		st = st + ch
	return st 

print "input : babblaaea, a \noutput:", fix_me("babblaaea", 'a')			

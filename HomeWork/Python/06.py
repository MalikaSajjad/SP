mylist = [1, 2 , 3, [4,5], "I am", "25", 3.4, 5.7, 65]
d = {}
for e in mylist:
	lst = d.get(type(e), [])
	lst.append(e)
	d[type(e)] = lst

print d
	


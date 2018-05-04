def both_ends(st):
	if len(st) < 2:
		return  ""
	else:
		st = st[0:2] + st[-2:]
		return st

print "input: spring \noutput :", both_ends("spring")
print "input: s \noutput : ", both_ends("s")

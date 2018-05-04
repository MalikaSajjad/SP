def match_ends(words):
	count = 0
	for st in words:
		if (len(st) >= 2) and (st[0] == st[-1]):
			count = count + 1
	return count

print "count : ",match_ends(['a', 'ab', 'abc', 'aba', 'aa', 'hye bye'])


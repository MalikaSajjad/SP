import sys
def mydict(y):
	d = {}
	for k in range(1, y+1):
		val = d.get(k,k*k)
		d[k] = val
	print d

if __name__ == "__main__":
	mydict(int(sys.argv[1]))

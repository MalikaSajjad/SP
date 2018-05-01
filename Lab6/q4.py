string = raw_input("enter comma separated values ")
lst = []
lst = string.split(",")
lst.sort()
string = lst[0]
for e in lst[1:]:
	string = string + string.join(",") + e
print string


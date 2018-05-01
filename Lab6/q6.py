string = raw_input("enter string ")
lst = string.split(" ")
set_ = set(lst)
lst = []
lst = list(set_)
lst.sort()
string = lst[0]
for e in lst[1:]:
	string = string + string.join(" ") + e
print string

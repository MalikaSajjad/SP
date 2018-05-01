string = raw_input("enter comma separated values ")
lst = []
tup = ()
lst = string.split(",")
tup = tuple(string.split(","))
print lst ,"|", tup

def remove_adjacent(nums):
	for indx, val in enumerate(nums):
		if len(nums)-1 > indx:
			if val == nums[indx + 1]:
				nums.pop(indx)
	return nums

print "list: [1,2,2,3,2] \nadajacent removed: ",remove_adjacent([1,2,2,3,2])
print "list: [1,2,2,3,2,2] \nadajacent removed: ", remove_adjacent([1,2,2,3,2,2])
print "list: [1,2,2,3,2,3] \nadajacent removed: ", remove_adjacent([1,2,2,3,2,3])

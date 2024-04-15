print('*********** Sets *************')
nums = { 1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))
print(len(nums2))

# No duplicates allowed in set
print()
print('*********** No duplicates allowed in set *************')
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
print()
print('*********** True is a dupe of 1, False is a dupe of zero *************')
nums = {1, True, 2, False, 3, 4, 5}
print(nums) 
# check if a value is in a set
print(2 in nums) 
#BUT can't refer to an element in a set with an index position or key

print()
print('*********** Add new element to a set *************')
nums.add(8)
print(nums)

print()
print('*********** Add elements from one set to another *************')
morenums = {5, 6, 7}
nums.update(morenums)
print(morenums)
print(nums)
# can use update with lists, tuples, & dictionaries, too.

print()
print('*********** merge two sets to create a new set *************')
setone = {1, 2, 3}
settwo = {4, 5, 6}

mynewset = setone.union(settwo)
print(mynewset)

print()
print('*********** Keep only the duplicates *************')
setone = {1, 2, 3}
settwo = {2, 3, 4, 5, 6}

setone.intersection_update(settwo)
print(setone)

print()
print('*********** Keep everything except the duplicates *************')
setone = {1, 2, 3}
settwo = {2, 3, 4, 5, 6}

setone.symmetric_difference_update(settwo)
print(setone)

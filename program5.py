# Use list comprehension to contruct a new list but add 6 to each item.
# 	list = [24,34,54,45]
first_list = [24, 34, 54, 45]

second_list = [num + 6 for num in first_list]

print("first list:", first_list)
print("after adding 6 to each item:", second_list)

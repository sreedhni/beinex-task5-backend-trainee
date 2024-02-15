# Using list comprehension, construct a list from the squares of each element in the list, 
# if the square is greater than 50.
# 	lst1=[2, 4, 6, 8, 10, 12, 14]

lst = [2, 4, 6, 8, 10, 12, 14]

squares_greaterthan50 = [n**2 for n in lst if n**2 > 50]

print("list with squares greater than 50:", squares_greaterthan50)

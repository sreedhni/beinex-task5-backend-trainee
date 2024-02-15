# 3.Write a Python program to count the number of strings where the string length is 2 or more.
# 	Sample List : ['abc', 'xyz', 'aba', '1']
# 	Expected Result : 3
def string_count(lst):
    count = 0
    for str in lst:
        if len(str) >= 2:
            count += 1
    return count

lst = ['abcd', 'xyz', 'a', '1']
Result = string_count(lst)
print("total number of strings with length 2 or more:", Result)

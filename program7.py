# 7. Write a Python program to find the repeated items of atuple.
def duplicate_items(tple):
    repeated_items = tuple(n for n in tple if tple.count(n) > 1)
    return repeated_items

given_tuple= (1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6)
duplicates = set(duplicate_items(given_tuple))
print("Repeated items in the tuple:", tuple(duplicates))

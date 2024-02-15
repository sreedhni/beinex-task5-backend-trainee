# Write a Python program to remove duplicates from a list
lst=[]
length=int(input("enter the length of the list; "))
for i in range(length):  
   element=input(f"enter {i} th element:")  
   lst.append(element) 
unique_lst = []
for l in lst:
        if l not in unique_lst:
            unique_lst.append(l)
print("list after removing duplicates;",unique_lst)
    

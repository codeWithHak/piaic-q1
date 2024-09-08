# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango","mango","banana"]
duplicates = []
unique_itmes = set()
for i in items:
    if i in unique_itmes:
       duplicates.append(i)     
    unique_itmes.add(i)


print("Unique items",duplicates)        

# print(items.count('a'))
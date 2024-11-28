#13. Find the Union of Two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union = list1[:]
for item in list2:
    if item not in union:
        union.append(item)
print("Union:", union)

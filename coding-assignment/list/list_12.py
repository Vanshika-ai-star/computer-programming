#12. Find the Intersection of Two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = []
for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)
print("Intersection:", intersection)

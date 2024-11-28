#19. Find the Difference Between Two Lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print("Difference:", difference)

#18. Write a Function to Find Common Elements in Two Lists
#Question: Create a function to find common elements between two lists.

def common_elements(lst1, lst2):
    common = []
    for item in lst1:
        if item in lst2 and item not in common:
            common.append(item)
    return common

print(common_elements([1, 2, 3], [3, 4, 5])) 

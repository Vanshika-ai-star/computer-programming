#13. Write a Function to Remove Duplicates from a List
#Question: Create a function to remove duplicate elements from a list.

def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicates([1, 2, 2, 3, 3, 3]))

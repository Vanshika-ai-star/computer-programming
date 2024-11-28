#17. Write a Function to Rotate a List
#Question: Create a function to rotate a list by k positions.

def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2)) 

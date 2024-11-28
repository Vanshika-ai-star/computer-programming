#11. Write a Function to Sort a List in Ascending Order
#Question: Create a function to sort a list in ascending order.

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(sort_list([4, 2, 8, 1, 3])) 

#10. Write a Function to Find the Maximum in a List
#Question: Create a function to find the maximum number in a list.

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([1, 5, 2, 9, 3])) 

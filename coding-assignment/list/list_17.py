#17. Remove a Specific Element from a List

numbers = [1, 2, 3, 4, 5]
target = 3
new_list = []
for num in numbers:
    if num != target:
        new_list.append(num)
print("List after removing", target, ":", new_list)

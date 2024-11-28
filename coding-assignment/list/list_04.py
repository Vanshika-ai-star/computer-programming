#4. Count Occurrences of an Element in a List

numbers = [1, 2, 3, 1, 4, 1, 5]
target = 1
count = 0
for num in numbers:
    if num == target:
        count += 1
print(f"Occurrences of {target}:", count)

#1. Find the Largest Number in a List
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)

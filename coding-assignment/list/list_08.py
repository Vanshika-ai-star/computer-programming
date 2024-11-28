#8. Find the Second Largest Number

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = numbers[0]
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest number:", second_largest)

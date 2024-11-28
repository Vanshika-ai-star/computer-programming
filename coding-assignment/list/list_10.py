#10. Sort a List in Ascending Order

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Sorted list:", numbers)

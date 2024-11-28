#2. Find the Smallest Number in a List

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)

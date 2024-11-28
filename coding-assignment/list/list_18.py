#18 Find the Pair with a Specific Sum
numbers = [2, 4, 3, 7, 1, 9]
target_sum = 10
found_pair = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            print(f"Pair found: {numbers[i]}, {numbers[j]}")
            found_pair = True
            break
    if found_pair:
        break

#5. Find the Index of an Element

numbers = [10, 20, 30, 40, 50]
target = 30
index = -1
for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break
print(f"Index of {target}:", index)

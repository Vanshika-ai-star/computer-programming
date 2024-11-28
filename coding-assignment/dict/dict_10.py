#10. Group Elements by Frequency
#Question: Write a program to group elements in a dictionary based on their frequency in a list.

lst = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for num in lst:
    frequency[num] = frequency.get(num, 0) + 1

grouped = {}
for key, value in frequency.items():
    if value not in grouped:
        grouped[value] = []
    grouped[value].append(key)

print("Grouped by Frequency:", grouped)  

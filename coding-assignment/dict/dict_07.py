#7. Count the Frequency of Elements in a List Using a Dictionary
#Question: Write a program to count the frequency of each element in a list using a dictionary.

lst = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for num in lst:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency Dictionary:", frequency)

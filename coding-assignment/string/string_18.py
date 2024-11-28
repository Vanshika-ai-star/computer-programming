#  Find the most frequent character in a string.
string = "banana"
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
most_frequent_char = max(frequency, key=frequency.get)
print(most_frequent_char) 

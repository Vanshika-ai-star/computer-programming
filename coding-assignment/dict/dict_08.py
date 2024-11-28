#8. Find the Maximum Value in a Dictionary
#Question: Write a program to find the key with the maximum value in a dictionary.

d = {"a": 10, "b": 20, "c": 15}
max_key = None
max_value = float('-inf')
for key, value in d.items():
    if value > max_value:
        max_value = value
        max_key = key
print(f"Key with maximum value: '{max_key}' -> {max_value}")

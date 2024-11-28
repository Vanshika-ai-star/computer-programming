#4. Remove a Key-Value Pair
#Question: Write a program to remove a specific key-value pair from a dictionary.

d = {"name": "Alice", "age": 25, "city": "New York"}
key_to_remove = "city"
if key_to_remove in d:
    del d[key_to_remove]
print("Dictionary after removal:", d)

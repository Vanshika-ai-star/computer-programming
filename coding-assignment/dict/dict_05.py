#5. Check if a Key Exists in a Dictionary
#Question: Write a program to check if a given key exists in a dictionary.

d = {"name": "Alice", "age": 25}
key = "city"
if key in d:
    print(f"'{key}' exists in the dictionary.")  # Output: (if key exists)
else:
    print(f"'{key}' does not exist in the dictionary.") 

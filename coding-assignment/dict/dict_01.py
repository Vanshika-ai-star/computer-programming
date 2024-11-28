#1. Access a Value in a Dictionary
#Question: Write a program to access and print the value of a given key in a dictionary.

d = {"name": "Alice", "age": 25, "city": "New York"}
key = "age"
if key in d:
    print(f"The value of '{key}' is:", d[key])  # Output: The value of 'age' is: 25
else:
    print(f"'{key}' not found in dictionary.")

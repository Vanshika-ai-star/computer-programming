#6. Merge Two Dictionaries
#Question: Write a program to merge two dictionaries into one.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = d1.copy()
for key, value in d2.items():
    merged_dict[key] = value
print("Merged Dictionary:", merged_dict)

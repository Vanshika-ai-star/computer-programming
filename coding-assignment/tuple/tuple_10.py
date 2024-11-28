#10. Convert a List of Tuples into a Dictionary
#Question: Write a program to convert a list of tuples into a dictionary.

tuples_list = [("a", 1), ("b", 2), ("c", 3)]
dictionary = {}
for key, value in tuples_list:
    dictionary[key] = value
print("Dictionary:", dictionary)

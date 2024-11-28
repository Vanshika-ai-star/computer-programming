#9. Reverse a Dictionary
#Question: Write a program to reverse a dictionary (swap keys and values).

d = {"a": 1, "b": 2, "c": 3}
reversed_dict = {}
for key, value in d.items():
    reversed_dict[value] = key
print("Reversed Dictionary:", reversed_dict) 

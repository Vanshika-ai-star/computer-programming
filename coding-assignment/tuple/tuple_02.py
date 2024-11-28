#2. Check if an Element Exists in a Tuple
#Question: Write a program to check if a given element exists in a tuple.

t = (1, 2, 3, 4, 5)
x = 3
if x in t:
    print(f"{x} exists in the tuple.") 
else:
    print(f"{x} does not exist in the tuple.")

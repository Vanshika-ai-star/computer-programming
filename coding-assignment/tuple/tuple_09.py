#9. Find the Length of a Tuple
#Question: Write a program to calculate the length of a tuple.

t = (1, 2, 3, 4, 5, 6)
length = 0
for _ in t:
    length += 1
print("Length of tuple:", length)

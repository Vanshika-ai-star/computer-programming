#4. Find the Index of an Element
#Question: Write a program to find the first occurrence index of an element in a tuple.

t = (10, 20, 30, 40, 50)
element = 30
index = -1
for i in range(len(t)):
    if t[i] == element:
        index = i
        break
print(f"Index of {element}:", index)

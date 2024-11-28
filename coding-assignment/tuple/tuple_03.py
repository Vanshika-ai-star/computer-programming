#3. Count Occurrences of an Element
#Question: Write a program to count how many times an element appears in a tuple.

t = (1, 2, 2, 3, 4, 2, 5)
element = 2
count = 0
for item in t:
    if item == element:
        count += 1
print(f"{element} occurs {count} times.")

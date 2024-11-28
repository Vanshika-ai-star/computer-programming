#8. Find the Largest and Smallest Elements in a Tuple
#Question: Write a program to find the largest and smallest elements in a tuple.

t = (10, 20, 5, 30, 15)
largest = t[0]
smallest = t[0]

for num in t:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest) 
print("Smallest:", smallest)  

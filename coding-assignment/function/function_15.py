#15. Write a Function to Flatten a Nested List
#Question: Create a function to flatten a nested list.

def flatten_list(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat

print(flatten_list([[1, 2], [3, 4], [5]]))

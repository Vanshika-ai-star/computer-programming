#12. Write a Function to Count the Frequency of Elements in a List
#Question: Create a function to count the frequency of each element in a list.

def frequency_count(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(frequency_count([1, 2, 2, 3, 3, 3])) 

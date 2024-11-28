#Q1: Remove Duplicate Characters from a String

# Input string
s = "banana"

# Remove duplicates using set and preserve order
unique_chars = "".join(sorted(set(s), key=s.index))

# Output
print(unique_chars)  

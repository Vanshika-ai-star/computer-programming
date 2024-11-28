# Remove Duplicate Characters from a String

s = "banana"
unique_chars = "".join(sorted(set(s), key=s.index))
print(unique_chars)  

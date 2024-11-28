#Q3: Check if Two Strings are Anagrams

# Input strings
s1 = "listen"
s2 = "silent"

# Check if both strings are anagrams by comparing sorted versions
if sorted(s1) == sorted(s2):
    print(True) 
else:
    print(False)

#Q3: Count Vowels in a String

# Input string
s = "hello"

# Count vowels
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1

# Output
print(count) 

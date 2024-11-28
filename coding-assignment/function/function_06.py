#6. Write a Function to Count Vowels
#Question: Create a function to count the number of vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  # Output: 3

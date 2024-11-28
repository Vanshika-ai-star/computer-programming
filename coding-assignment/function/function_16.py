#16. Write a Function to Check for a Substring
#Question: Create a function to check if a string contains a specific substring.

def contains_substring(string, substring):
    return substring in string

print(contains_substring("hello world", "world"))

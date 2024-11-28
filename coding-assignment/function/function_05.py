#5. Write a Function to Check for Palindromes
Question: Create a function that checks if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) 

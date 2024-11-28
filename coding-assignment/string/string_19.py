# Replace Substring in a String
Question: Write a program to replace a substring with another substring in a string.

def replace_substring(s, old, new):
    return s.replace(old, new)

# Example usage
string = "hello world"
print("Modified string:", replace_substring(string, "world", "Python"))

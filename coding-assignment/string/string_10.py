# 9. Replace all vowels in a string with '*'.
string = "hello world"
vowels = "aeiouAEIOU"
replaced_string = "".join('*' if char in vowels else char for char in string)
print(replaced_string) 

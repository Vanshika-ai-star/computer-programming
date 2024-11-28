#  Check if a string contains only alphabets without using isalpha().
string = "hello"
is_alpha = all(('a' <= char <= 'z') or ('A' <= char <= 'Z') for char in string)
print(is_alpha) 

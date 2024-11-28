# 6. Convert a string to uppercase without using the upper() method.
string = "hello"
uppercase_string = "".join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in string)
print(uppercase_string)  

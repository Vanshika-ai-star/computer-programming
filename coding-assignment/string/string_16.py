#  Remove all numeric digits from a string.
string = "hello123world"
no_digits = "".join(char for char in string if not ('0' <= char <= '9'))
print(no_digits)  

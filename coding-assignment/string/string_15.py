#  Find the first non-repeating character in a string.
string = "swiss"
non_repeating_char = None
for char in string:
    if string.count(char) == 1:
        non_repeating_char = char
        break
print(non_repeating_char)  

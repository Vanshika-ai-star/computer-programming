# Convert to Lowercase
string = "HELLO WORLD"
lowercase_string = ""
for char in string:
    if "A" <= char <= "Z":
        lowercase_string += chr(ord(char) + 32)
    else:
        lowercase_string += char
print("Lowercase string:", lowercase_string)

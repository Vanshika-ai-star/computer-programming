#  Replace all occurrences of a substring without using replace().
string = "hello world"
old = "world"
new = "Python"
result = ""
for word in string.split():
    if word == old:
        result += new + " "
    else:
        result += word + " "
print(result.strip())  

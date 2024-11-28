#  Check if a string contains only digits.
string = "12345"
is_digit = all('0' <= char <= '9' for char in string)
print(is_digit) 

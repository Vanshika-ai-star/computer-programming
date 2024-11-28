#14. Write a Function to Find the Power of a Number
#Question: Create a function to calculate the power of a number x^y.

def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

print(power(2, 3))

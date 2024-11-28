#2. Write a Function to Find the Factorial of a Number
Question: Create a function to compute the factorial of a given number.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5)) 

#4. Write a Function to Find the GCD of Two Numbers
Question: Create a function that calculates the greatest common divisor (GCD).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(36, 60))  

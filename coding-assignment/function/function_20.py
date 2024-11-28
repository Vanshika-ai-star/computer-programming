#20. Write a Function to Check for Perfect Numbers
#Question: Create a function to check if a number is perfect (sum of divisors equals the number).

def is_perfect(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

print(is_perfect(28))

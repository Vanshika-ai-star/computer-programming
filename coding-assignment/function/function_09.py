#9. Write a Function to Generate Fibonacci Sequence
#Question: Create a function to generate the first n terms of the Fibonacci sequence.

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

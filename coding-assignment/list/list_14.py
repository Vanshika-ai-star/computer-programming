#14. Rotate a List to the Left

numbers = [1, 2, 3, 4, 5]
k = 2  # Number of rotations
rotated_list = numbers[k:] + numbers[:k]
print("Left rotated list:", rotated_list)

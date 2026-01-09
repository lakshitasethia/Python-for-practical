# Create a 4x4 matrix and calculate the sum of its main diagonal elements
import numpy as np
import random

arr = np.random.randint(1, 10, size=(4, 4))
print(arr)
print(np.sum(np.diagonal(arr)))
print('-'*100)

# Generate a 3x3 matrix and find the smallest value among all its elements.
arr2 = np.random.randint(1, 10, size=(3, 3))
print(arr2)
print(np.min(arr2))
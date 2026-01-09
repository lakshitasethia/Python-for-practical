# Generate a 6x6 matrix of random integers and replace all values below the median with zero

import numpy as np
import random

arr = np.random.randint(1, 10, size=(6, 6))
median_value = np.median(arr)
arr[arr < median_value] = 0
print(arr)
print('-'*100)

# Create a 4x4 matrix and compute the sum of elements in the upper triangular part of the matrix.
arr2 = np.random.randint(1, 10, size=(4, 4))
print(arr2)
upper_triangular_sum = np.sum(np.triu(arr2))
print(upper_triangular_sum)
print('-'*100)

# Generate a 3x4 matrix of random values and find the standard deviation of the elements in the third column.
arr3 = np.random.randint(1, 10, size=(3, 4))
print(arr3)
third_column = arr3[:, 2]
print(np.std(third_column))
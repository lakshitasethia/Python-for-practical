# Create a 2x3 matrix and find the sum of all elements in the second row.
import numpy as np
import random

arr = np.random.randint(1, 10, size=(2, 3))
sliced_arr = arr[1:, 0:3]
print(arr)
print(np.sum(sliced_arr))

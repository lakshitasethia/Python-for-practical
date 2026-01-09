# Generate a 4x4 matrix of random numbers and compute the average of all its elements.

import numpy as np
import random

arr = np.random.randint(1, 10, size=(4, 4))
print(arr)
print(arr.shape)
print(arr.size)
print(f"The average of the matrix is {np.average(arr)}")

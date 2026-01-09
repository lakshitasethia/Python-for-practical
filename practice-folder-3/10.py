# Given an integer N, create an N×N NumPy array filled with values from 1 to N*N. Extract and print the middle (N-2)×(N-2) submatrix.

import numpy as np
import random
dimension=int(input("Enter the dimension of the square matrix: "))

arr = np.random.randint(1, (dimension**2)+1, size=(dimension, dimension))
print(arr)
print(arr[1:dimension-1,1:dimension-1])
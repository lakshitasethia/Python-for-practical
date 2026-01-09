# Create a 4×4 NumPy matrix with values from 1 to 16. Swap the first and last row
import numpy as np
import random

arr = np.random.randint(1, 17, size=(4, 4))
print(arr)
print('-'*100)
first_row = arr[0, :]
last_row = arr[3, :]
first_row, last_row = last_row.copy(), first_row.copy()
arr[0, :] = first_row
arr[3, :] = last_row
print(arr) 

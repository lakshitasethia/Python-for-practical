# Create a 4x4 matrix of random integers between 1 and 20 and compute the sum of all elements that are greater than 10.

import numpy as np
import random

arr = np.random.randint(1, 20, size=(4, 4))
selected_elements = arr[arr > 10]
print(arr)
print(np.sum(selected_elements))
print('-'*100)

# Generate a 5x5 matrix of random numbers between 1 to 10 and find the mean of the maximum values of each row.

arr2 = np.random.randint(1, 10, size=(5, 5))
max_of_all_rows=(np.max(arr2,axis=1))
print(arr2)
print(np.mean(max_of_all_rows))
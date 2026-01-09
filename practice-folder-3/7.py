# Create a 3x3 matrix and calculate the difference between the sum of the elements in the first row and the sum of the elements in the last row.

import numpy as np
import random
import math

arr = np.random.randint(1, 10, size=(3, 3))
print(arr)
first_row_sum=np.sum(np.array(arr[0,:3]))
last_row_sum=np.sum(np.array(arr[2,:3]))
print(abs(first_row_sum - last_row_sum))
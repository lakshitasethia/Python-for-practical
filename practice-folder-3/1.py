# Create a 3x3 matrix of random integers between 1 and 10 and find the total sum of its elements.

import numpy as np
import random
arr=np.random.randint(1,10,size=(3,3))
print(arr)
print(np.sum(arr))
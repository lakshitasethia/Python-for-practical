# Generate a NumPy array of size 1000 containing random integers between 1 and 100. Print the frequency of each number.
import numpy as np
import random
arr = np.random.randint(1, 101, size=1000)
print(arr.reshape(10,100))
# unique_values, counts = np.unique(arr, return_counts=True)
# for value, count in zip(unique_values, counts):
#     print(f"{value} -> {count}")
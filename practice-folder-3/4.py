# Generate a 5x5 matrix of random integers and determine the highest value in each column.
import numpy as np
import random

arr = np.random.randint(1, 10, size=(5, 5))
print(arr)
column_0 = arr[:,0]
column_1 = arr[:,1]
column_2 = arr[:,2]
column_3 = arr[:,3]
column_4 = arr[:,4]
print(f"Max of colum 0: {np.max(column_0)}")
print(f"Max of colum 1: {np.max(column_1)}")
print(f"Max of colum 2: {np.max(column_2)}")
print(f"Max of colum 3: {np.max(column_3)}")
print(f"Max of colum 4: {np.max(column_4)}")


# better method
all_columns=np.max(arr, axis=0)
print(f"\nMax of all columns: {all_columns}")
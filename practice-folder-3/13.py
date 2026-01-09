import numpy as np
import random

arr = np.zeros((4,4))
np.fill_diagonal(arr, 1)
print(arr)

hours_studied = [1, 2, 3, 4, 5]
test_scores = [50, 60, 70, 80, 90]

correlation = np.corrcoef(hours_studied, test_scores)[0, 1]
print(correlation)
# Result: ~1.0 (more study = higher score!)

from scipy import stats
data = np.array([4, 1, 2, 2, 3, 4, 4])

# New way (SciPy 1.9+):
mode = stats.mode(data, keepdims=True).mode[0]
print(mode)

# OR the simple NumPy way (no scipy needed!):
values, counts = np.unique(data, return_counts=True)
mode = values[counts.argmax()]
print(mode)  # Gets the value with highest count
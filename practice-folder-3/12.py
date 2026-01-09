import numpy as np
import random

arr1 = [10, 20, 30, 40, 50]
result=[]
value=11
for element in arr1:
    element=abs(element - value)
    result.append(element)
# Find which position has minimum distance
min_index = result.index(min(result))  # Position of smallest distance
closest_element = arr1[min_index]      # Get element at that position

print("Closest element:", closest_element)  # Output: 10

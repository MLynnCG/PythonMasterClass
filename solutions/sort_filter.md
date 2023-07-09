
```python
import numpy as np

# 1. Create the array
arr = np.array([8, 5, 2, 9, 4, 1])

# 2. Sort the array in ascending order
sorted_arr = np.sort(arr)
print("Sorted array:")
print(sorted_arr)

# 3. Sort the array in descending order
desc_sorted_arr = np.sort(arr)[::-1]
print("Array sorted in descending order:")
print(desc_sorted_arr)

# 4. Find unique elements in the array
unique_elements = np.unique(arr)
print("Unique elements:")
print(unique_elements)

# 5. Filter the array based on a condition
filtered_arr = arr[arr > 4]
print("Filtered array (elements > 4):")
print(filtered_arr)
```

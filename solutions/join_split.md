
```python
import numpy as np

# 1. Create the arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# 2. Concatenate along the rows (vertical stacking)
vertical_stack = np.vstack((arr1, arr2))
print("Vertical stack:")
print(vertical_stack)

# 3. Concatenate along the columns (horizontal stacking)
horizontal_stack = np.hstack((arr1.reshape(-1, 1), arr2.reshape(-1, 1)))
print("Horizontal stack:")
print(horizontal_stack)

# 4. Create the array to be split
split_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 5. Split the array into three sub-arrays
sub_array1, sub_array2, sub_array3 = np.split(split_arr, [3, 7])
print("Sub-array 1:")
print(sub_array1)
print("Sub-array 2:")
print(sub_array2)
print("Sub-array 3:")
print(sub_array3)
```

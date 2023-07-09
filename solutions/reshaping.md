```python
import numpy as np

# 1. Create the array
nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 2. Print the shape of the array
print("Original array shape:", nums.shape)

# 3. Reshape the array
reshaped_nums = nums.reshape(5, 2)

# 4. Print the shape of the reshaped array
print("Reshaped array shape:", reshaped_nums.shape)

# 5. Flatten the array
flattened_nums = reshaped_nums.flatten()

# 6. Print the shape of the flattened array
print("Flattened array shape:", flattened_nums.shape)

# 7. Transpose the array
transposed_nums = reshaped_nums.T

# 8. Print the shape of the transposed array
print("Transposed array shape:", transposed_nums.shape)
```

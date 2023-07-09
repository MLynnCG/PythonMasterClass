```python
import numpy as np

# 1. Create the array
nums = np.array([3, 7, 1, 9, 5])

# 2. Compute the mean
mean_value = np.mean(nums)
print("Mean:", mean_value)

# 3. Compute the median
median_value = np.median(nums)
print("Median:", median_value)

# 4. Compute the standard deviation
std_value = np.std(nums)
print("Standard Deviation:", std_value)

# 5. Compute the variance
variance_value = np.var(nums)
print("Variance:", variance_value)

# 6. Create the matrix
matrix = np.array([[2, 4],
                   [6, 8]])

# 7. Compute the transpose
transposed_matrix = matrix.T
print("Transposed Matrix:")
print(transposed_matrix)

# 8. Compute matrix multiplication
mult_result = np.matmul(matrix, transposed_matrix)
print("Matrix Multiplication:")
print(mult_result)

# 9. Compute the inverse
inverse_matrix = np.linalg.inv(matrix)
print("Inverse Matrix:")
print(inverse_matrix)

# 10. Compute the determinant
determinant_value = np.linalg.det(matrix)
print("Determinant:", determinant_value)
```

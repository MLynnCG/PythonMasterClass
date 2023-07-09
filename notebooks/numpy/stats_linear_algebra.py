import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Statistics operations
print("Mean:", np.mean(arr))                   # Compute the mean of the array
print("Median:", np.median(arr))               # Compute the median of the array
print("Standard Deviation:", np.std(arr))      # Compute the standard deviation of the array
print("Variance:", np.var(arr))                # Compute the variance of the array

# Linear algebra operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("\nMatrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

print("\nMatrix Transpose:")
print(matrix1.T)                             # Compute the transpose of the matrix

print("\nMatrix Multiplication:")
print(np.matmul(matrix1, matrix2))            # Perform matrix multiplication

print("\nMatrix Inverse:")
print(np.linalg.inv(matrix1))                 # Compute the inverse of the matrix

print("\nMatrix Determinant:")
print(np.linalg.det(matrix1))                 # Compute the determinant of the matrix

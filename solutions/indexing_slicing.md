```python
import numpy as np

# 1. Create the matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# 2. Access and print an element
print("Element at second row, third column:", matrix[1, 2])

# 3. Access and print the second column
second_column = matrix[:, 1]
print("Second column:", second_column)

# 4. Modify an element
matrix[2, 3] = 99

# 5. Create a submatrix
submatrix = matrix[:2, :3]

# 6. Print the results
print("Matrix:")
print(matrix)
print("Extracted element:", matrix[1, 2])
print("Extracted column:", second_column)
print("Modified matrix:")
print(matrix)
print("Submatrix:")
print(submatrix)
```

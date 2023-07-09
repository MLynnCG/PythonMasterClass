
```python
import numpy as np

# 1. Create the matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 2. Access and print an element
print("Element at second row, third column:", matrix[1, 2])

# 3. Extract the second column
column = matrix[:, 1]
print("Extracted column:", column)

# 4. Modify an element
matrix[0, 1] = 10

# 5. Reshape the matrix
flattened_array = matrix.reshape(-1)
print("Flattened array:", flattened_array)

# 6. Concatenate arrays
concatenated_array = np.concatenate((column, flattened_array), axis=0)
print("Concatenated array:", concatenated_array)

# 7. Split the concatenated array
sub_array1, sub_array2, sub_array3 = np.split(concatenated_array, 3)
print("Sub-array 1:", sub_array1)
print("Sub-array 2:", sub_array2)
print("Sub-array 3:", sub_array3)

# 8. Print the results
print("Matrix:")
print(matrix)
print("Column:")
print(column)
print("Flattened array:")
print(flattened_array)
print("Concatenated array:")
print(concatenated_array)
print("Sub-array 1:")
print(sub_array1)
print("Sub-array 2:")
print(sub_array2)
print("Sub-array 3:")
print(sub_array3)
```

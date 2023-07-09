
```python
import numpy as np

# 1. Create the arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# 2. Perform array operations
print("Element-wise addition:", arr1 + arr2)
print("Element-wise subtraction:", arr1 - arr2)
print("Element-wise multiplication:", arr1 * arr2)
print("Element-wise division:", arr1 / arr2)
print("Element-wise exponentiation:", arr1 ** arr2)

# 3. Scalar operation on arr1
arr3 = arr1 + 5
print("Scalar addition:", arr3)

# 4. Scalar operation on arr2
arr4 = arr2 * 3
print("Scalar multiplication:", arr4)

# 5. Logical operations
print("Element-wise comparison (arr1 < 3):", arr1 < 3)
print("Element-wise comparison (arr2 >= 7):", arr2 >= 7)
print("Element-wise logical NOT:", np.logical_not(arr1))
print("Element-wise logical AND:", np.logical_and(arr1, arr2))
```

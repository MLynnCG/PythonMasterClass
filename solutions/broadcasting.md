
```python
import numpy as np

# 1. Create the arrays
arr1 = np.array([1, 2, 3])

# 2. Scalar broadcasting
scalar_broadcast = arr1 * 3
print("Scalar Broadcasting:")
print(scalar_broadcast)

# 3. Create the second array
arr2 = np.array([[4, 5, 6],
                 [7, 8, 9]])

# 4. Array broadcasting
array_broadcast = arr1 + arr2
print("\nArray Broadcasting:")
print(array_broadcast)

# 5. Create the third array
arr3 = np.array([10, 20])

# Broadcasting with arrays of different dimensions
broadcast_result = arr1 + arr3[:, np.newaxis]
print("\nBroadcasting with Different Dimensions:")
print(broadcast_result)
```

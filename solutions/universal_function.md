
```python
import numpy as np

# 1. Create the array
nums = np.array([1, 2, 3, 4, 5])

# 2. Perform ufunc operations
print("Original array:", nums)
print("Square root:", np.sqrt(nums))
print("Exponential:", np.exp(nums))
print("Natural logarithm:", np.log(nums))
print("Sine:", np.sin(nums))
print("Cosine:", np.cos(nums))
print("Element-wise addition:", np.add(nums, 3))
print("Element-wise subtraction:", np.subtract(nums, 2))
print("Element-wise multiplication:", np.multiply(nums, 4))
print("Element-wise division:", np.divide(nums, 2))
print("Element-wise maximum:", np.maximum(nums, [2, 4, 6, 1, 5]))
print("Element-wise minimum:", np.minimum(nums, [3, 1, 5, 4, 2]))
```

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Universal Functions (ufuncs)
print("Original array:", arr)
print("Square root:", np.sqrt(arr))          # Compute the square root of each element
print("Exponential:", np.exp(arr))           # Compute the exponential of each element
print("Natural logarithm:", np.log(arr))      # Compute the natural logarithm of each element
print("Sine:", np.sin(arr))                   # Compute the sine of each element
print("Cosine:", np.cos(arr))                 # Compute the cosine of each element
print("Element-wise addition:", np.add(arr, 2))      # Add a scalar value to each element
print("Element-wise subtraction:", np.subtract(arr, 2))  # Subtract a scalar value from each element
print("Element-wise multiplication:", np.multiply(arr, 2))  # Multiply each element by a scalar value
print("Element-wise division:", np.divide(arr, 2))      # Divide each element by a scalar value
print("Element-wise maximum:", np.maximum(arr, [3, 2, 4, 5, 1]))  # Element-wise maximum between two arrays
print("Element-wise minimum:", np.minimum(arr, [3, 2, 4, 5, 1]))  # Element-wise minimum between two arrays

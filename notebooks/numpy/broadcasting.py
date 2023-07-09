import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3])

# Scalar broadcasting
scalar = 2
scalar_broadcast = arr * scalar
print("Scalar Broadcasting:")
print(scalar_broadcast)

# Array broadcasting
array = np.array([[4], [5], [6]])
array_broadcast = arr * array
print("\nArray Broadcasting:")
print(array_broadcast)

# Broadcasting with different dimensions
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4], [5]])
broadcast_result = arr1 + arr2
print("\nBroadcasting with Different Dimensions:")
print(broadcast_result)

import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])

# Shape of a NumPy array
print("Original array:", arr)
print("Shape of the array:", arr.shape)

# Reshaping a NumPy array
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped array (2 rows, 3 columns):")
print(reshaped_arr)
print("Shape of the reshaped array:", reshaped_arr.shape)

# Reshaping with -1 (automatic computation)
reshaped_arr_auto = arr.reshape(3, -1)
print("\nReshaped array with automatic computation (3 rows, automatic columns):")
print(reshaped_arr_auto)
print("Shape of the reshaped array with automatic computation:", reshaped_arr_auto.shape)

# Flattening a NumPy array
flattened_arr = reshaped_arr.flatten()
print("\nFlattened array:")
print(flattened_arr)
print("Shape of the flattened array:", flattened_arr.shape)

# Transposing a NumPy array
transposed_arr = reshaped_arr.T
print("\nTransposed array:")
print(transposed_arr)
print("Shape of the transposed array:", transposed_arr.shape)

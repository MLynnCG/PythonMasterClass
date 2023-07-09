import numpy as np
import numpy.ma as ma

# Create a regular NumPy array
arr = np.array([1, 2, 3, -999, 5])

# Create a masked array
masked_arr = ma.masked_values(arr, -999)

# Print the masked array
print("Masked Array:")
print(masked_arr)

# Accessing data and mask of the masked array
print("\nData:", masked_arr.data)
print("Mask:", masked_arr.mask)

# Applying operations on masked arrays
mean = ma.mean(masked_arr)
print("\nMean:", mean)

# Creating a mask manually
mask = [False, False, False, True, False]
masked_arr_manual = ma.masked_array(arr, mask)

# Print the manually masked array
print("\nManually Masked Array:")
print(masked_arr_manual)

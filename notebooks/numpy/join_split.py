import numpy as np

# Create two NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Array concatenation
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated array:")
print(concatenated_arr)

# Create a 2D NumPy array
arr3 = np.array([[7, 8, 9],
                 [10, 11, 12]])

# Array concatenation along the rows (vertical stacking)
vertical_stack = np.vstack((arr1, arr3))
print("\nVertical stack:")
print(vertical_stack)

# Array concatenation along the columns (horizontal stacking)
horizontal_stack = np.hstack((arr1.reshape(-1, 1), arr2.reshape(-1, 1)))
print("\nHorizontal stack:")
print(horizontal_stack)

# Array splitting
split_arr = np.array([1, 2, 3, 4, 5, 6])
split_result = np.split(split_arr, [2, 4])
print("\nSplit arrays:")
print(split_result)

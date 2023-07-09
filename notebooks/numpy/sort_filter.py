import numpy as np

# Create a NumPy array
arr = np.array([4, 2, 9, 1, 7, 5])

# Sorting the array
sorted_arr = np.sort(arr)
print("Sorted array:")
print(sorted_arr)

# Sorting the array in descending order
desc_sorted_arr = np.sort(arr)[::-1]
print("\nArray sorted in descending order:")
print(desc_sorted_arr)

# Finding unique elements in the array
unique_elements = np.unique(arr)
print("\nUnique elements:")
print(unique_elements)

# Filtering the array based on a condition
filtered_arr = arr[arr > 4]
print("\nFiltered array (elements > 4):")
print(filtered_arr)

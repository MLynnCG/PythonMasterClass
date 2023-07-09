import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Iterate over rows
print("Iterating over rows:")
for row in arr:
    print(row)

# Iterate over elements
print("\nIterating over elements:")
for row in arr:
    for element in row:
        print(element)

# Iterate using nditer
print("\nIterating using nditer:")
for element in np.nditer(arr):
    print(element)

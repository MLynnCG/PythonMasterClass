```python
import numpy as np

# 1. Create the array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# 2. Iterate over rows
print("Iterating over rows:")
for row in arr:
    print(row)

# 3. Iterate over elements
print("\nIterating over elements:")
for row in arr:
    for element in row:
        print(element)

# 4. Iterate using nditer
print("\nIterating using nditer:")
for element in np.nditer(arr):
    print(element)
```
Subscribe to my youtube channel

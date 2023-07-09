import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# Print the DataFrame
print("Pandas DataFrame:")
print(df)

# Accessing DataFrame elements using NumPy indexing
print("\nAccessing DataFrame elements using NumPy indexing:")
print(df.values[1, 2])     # Access the element in the second row and third column

# Accessing DataFrame elements using Pandas indexing
print("\nAccessing DataFrame elements using Pandas indexing:")
print(df.loc[2, 'B'])      # Access the element in the third row and 'B' column

# Performing computations with NumPy on DataFrame columns
df['D'] = np.sqrt(df['C'])
print("\nDataFrame after adding column 'D' with square root of 'C':")
print(df)

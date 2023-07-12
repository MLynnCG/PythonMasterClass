## Solutions for the exercise of read_save_data

import numpy as np
import pandas as pd

# 1. Create a NumPy array
array = np.random.randint(1, 101, size=(5, 3))

# 2. Save the array in NumPy format
np.save('my_array.npy', array)
print("Array saved in NumPy format as 'my_array.npy'.")

# 3. Save the array in text format
np.savetxt('my_array.txt', array, delimiter=',')
print("Array saved in text format as 'my_array.txt'.")

# 4. Save the array in CSV format
df = pd.DataFrame(array)
df.to_csv('my_array.csv', index=False)
print("Array saved in CSV format as 'my_array.csv'.")

# 5. Create another NumPy array
another_array = np.random.random((4, 2))

# 6. Save both arrays in a compressed format
np.savez('combined_arrays.npz', array=array, another_array=another_array)
print("Arrays saved in compressed format as 'combined_arrays.npz'.")

# 7. Print the shapes of the loaded arrays
loaded_array = np.load('my_array.npy')
loaded_text_array = np.loadtxt('my_array.txt', delimiter=',')
loaded_csv_array = pd.read_csv('my_array.csv')
compressed_arrays = np.load('combined_arrays.npz')
loaded_combined_array = compressed_arrays['array']
loaded_combined_another_array = compressed_arrays['another_array']

print("\nShapes of Loaded Arrays:")
print("my_array.npy:", loaded_array.shape)
print("my_array.txt:", loaded_text_array.shape)
print("my_array.csv:", loaded_csv_array.shape)
print("combined_arrays.npz (array):", loaded_combined_array.shape)
print("combined_arrays.npz (another_array):", loaded_combined_another_array.shape)

# 8. Load and print the arrays from combined_arrays.npz
print("\nLoaded Arrays from combined_arrays.npz:")
print("Array:")
print(loaded_combined_array)
print("Another Array:")
print(loaded_combined_another_array)

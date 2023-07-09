import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Save array to a file
np.savetxt('array.txt', arr, delimiter=',')

# Load array from a file
loaded_arr = np.loadtxt('array.txt', delimiter=',')
print("Loaded array:")
print(loaded_arr)

# Generate random numbers
random_nums = np.random.random(size=(3, 4))
print("\nRandom numbers:")
print(random_nums)

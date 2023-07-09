```python
import numpy as np

# 1. Create the array
nums = np.array([1, 2, 3, 4, 5])

# 2. Save the array to a file
np.savetxt('numbers.txt', nums, delimiter=',')

# 3. Load the array from the file
loaded_nums = np.loadtxt('numbers.txt', delimiter=',')
print("Loaded array:")
print(loaded_nums)

# 4. Verify the loaded array
print("Arrays match:", np.array_equal(nums, loaded_nums))

# 5. Generate a 2D random array
random_arr = np.random.random(size=(3, 4))
print("\nRandom array:")
print(random_arr)
```

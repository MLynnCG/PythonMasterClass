```python
import numpy as np
import numpy.ma as ma

# 1. Create the array
data = np.array([10, 20, -999, 30, 40, -999, 50])

# 2. Create the masked array
masked_data = ma.masked_values(data, -999)

# 3. Print the masked array
print("Masked Array:")
print(masked_data)

# 4. Calculate the mean
mean_value = ma.mean(masked_data)
print("Mean:", mean_value)

# 5. Create the manual mask
mask = data > 30

# 6. Create the masked array using manual mask
masked_data_manual = ma.masked_array(data, mask)

# 7. Print the manually masked array
print("Manually Masked Array:")
print(masked_data_manual)
```

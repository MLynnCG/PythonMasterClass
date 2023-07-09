# Exercise 1: Creating a DataFrame from NumPy array and performing calculations
Instructions:
1. Create a 2D NumPy array called `data` with the following elements:
   ```
   [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
   ```

2. Convert the `data` array into a Pandas DataFrame called `df` with columns named 'A', 'B', and 'C'.

3. Calculate the sum of each column in the DataFrame using NumPy's `np.sum()` function, and store the result in a new variable called `column_sums`.

4. Print the column sums.

You can solve this exercise by adding code to the previous Python code block or by creating a new code block.

```python
import numpy as np
import pandas as pd

# 1. Create the NumPy array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# 2. Convert the array to a DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 3. Calculate the column sums
column_sums = np.sum(df, axis=0)

# 4. Print the column sums
print("Column Sums:")
print(column_sums)
```

Exercise 2: Filtering DataFrame using NumPy condition

Instructions:
1. Create a DataFrame called `df` with the following data:
   ```
   Name    Age    City
   John    25     London
   Alice   32     Paris
   Bob     28     New York
   Sarah   22     London
   ```

2. Use NumPy to filter the DataFrame and create a new DataFrame called `filtered_df` that contains only the rows where the 'City' column is 'London'.

3. Print the `filtered_df`.

```python
import numpy as np
import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Sarah'],
    'Age': [25, 32, 28, 22],
    'City': ['London', 'Paris', 'New York', 'London']
}
df = pd.DataFrame(data)

# 2. Filter the DataFrame
filtered_df = df[np.array(df['City'] == 'London')]

# 3. Print the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)
```

Exercise 3: Performing calculations on DataFrame columns using NumPy functions

Instructions:
1. Create a DataFrame called `df` with the following data:
   ```
   Name    Height (cm)    Weight (kg)
   John    175            70
   Alice   163            55
   Bob     180            82
   Sarah   168            63
   ```

2. Use NumPy functions to calculate the Body Mass Index (BMI) for each person and store the result in a new column called 'BMI' in the DataFrame. The BMI can be calculated using the formula: BMI = weight (kg) / (height (m))^2.

3. Print the updated DataFrame with the 'BMI' column.

```python
import numpy as np
import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Sarah'],
    'Height (cm)': [175, 163, 180, 168],
    'Weight (kg)': [70, 55, 82, 63]
}
df = pd.DataFrame(data)

# 2. Calculate BMI using NumPy functions
height_m = df['Height (cm)'] / 100  # Convert height from cm to m
bmi = df['Weight (kg)'] / np.power(height_m, 2)
df['BMI'] = bmi

# 3. Print the updated DataFrame
print("Updated DataFrame:")
print(df)
```


# Exercise: Masked Arrays
Instructions:
1. Create a NumPy array called `data` with the following elements:
   ```
   [10, 20, -999, 30, 40, -999, 50]
   ```

2. Create a masked array called `masked_data` from the `data` array, where the value -999 is masked.

3. Print the `masked_data` array.

4. Calculate the mean of the `masked_data` array using the `ma.mean()` function and store the result in a variable called `mean_value`.

5. Create a manual mask called `mask` that masks all values greater than 30 in the `data` array.

6. Create a masked array called `masked_data_manual` from the `data` array and the `mask` using the `ma.masked_array()` function.

7. Print the `masked_data_manual` array.




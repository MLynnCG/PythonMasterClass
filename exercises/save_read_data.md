# Exercise: Saving and Sharing NumPy Arrays

## Instructions:
1. Create a NumPy array with random integer values between 1 and 100 (inclusive) of shape (5, 3). Assign it to the variable `array`.
2. Save the `array` in NumPy format as 'my_array.npy'.
3. Save the `array` in text format as 'my_array.txt' with a comma (',') as the delimiter.
4. Save the `array` in CSV format as 'my_array.csv'.
5. Create a new NumPy array with random float values between 0 and 1 of shape (4, 2). Assign it to the variable `another_array`.
6. Save both `array` and `another_array` in a compressed format as 'combined_arrays.npz' using `np.savez()` or `np.savez_compressed()`.
7. Print the shapes of the loaded arrays from 'my_array.npy', 'my_array.txt', 'my_array.csv', and 'combined_arrays.npz'.
8. Load the 'combined_arrays.npz' file and print the arrays 'array' and 'another_array' stored inside it.
9. Bonus: Share the 'my_array.npy' file with a friend or colleague and ask them to load and print the array.

Note: Remember to import the necessary libraries (`numpy` and `pandas`) before starting the exercise.

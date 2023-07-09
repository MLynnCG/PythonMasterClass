import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)   # Create an array of 100 evenly spaced values from 0 to 10
y = np.sin(x)                  # Compute the sine of each value in the x array

# Plotting the data
plt.plot(x, y)                 # Plot x versus y
plt.xlabel('x')                # Set the x-axis label
plt.ylabel('sin(x)')           # Set the y-axis label
plt.title('Plot of sin(x)')    # Set the title of the plot
plt.grid(True)                 # Enable grid lines
plt.show()                     # Display the plot

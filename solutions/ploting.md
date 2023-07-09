
```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Create the x-coordinates
x = np.linspace(-5, 5, 100)

# 2. Create the y-coordinates
y = x**2

# 3. Plot x versus y
plt.plot(x, y)

# 4. Set x-axis and y-axis labels
plt.xlabel('x')
plt.ylabel('y')

# 5. Set the title
plt.title('Plot of y = x^2')

# 6. Enable grid lines
plt.grid(True)

# 7. Display the plot
plt.show()
```

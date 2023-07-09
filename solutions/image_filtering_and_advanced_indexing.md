Certainly! Here's an exercise for practicing image filtering and advanced indexing in NumPy:


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# 1. Load the image
image = plt.imread('image.jpg')

# 2. Display the original image
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')

# 3. Convert the image to grayscale
gray_image = np.mean(image, axis=2)

# 4. Apply a median filter to the grayscale image
filtered_image = ndimage.median_filter(gray_image, size=5)

# 5. Display the filtered image
plt.subplot(1, 3, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')

# 6. Apply advanced indexing to extract a region of interest (ROI)
roi = filtered_image[100:300, 200:400]

# 7. Display the extracted ROI
plt.subplot(1, 3, 3)
plt.imshow(roi, cmap='gray')
plt.title('Region of Interest')

plt.tight_layout()
plt.show()
```

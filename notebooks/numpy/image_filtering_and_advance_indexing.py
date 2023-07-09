import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# Load an image
image = plt.imread('image.jpg')

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

# Convert the image to grayscale
gray_image = np.mean(image, axis=2)

# Apply a Gaussian filter to the grayscale image
filtered_image = ndimage.gaussian_filter(gray_image, sigma=3)

# Display the filtered image
plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')

# Apply advanced indexing to extract a region of interest (ROI) from the filtered image
roi = filtered_image[100:300, 200:400]

# Display the ROI
plt.figure()
plt.imshow(roi, cmap='gray')
plt.title('Region of Interest')

plt.tight_layout()
plt.show()

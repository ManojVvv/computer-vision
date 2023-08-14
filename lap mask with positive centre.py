import cv2
import numpy as np

# Load the image
image_path = 'spyder.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise before applying Laplacian filter
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)

# Define the Laplacian kernel with a positive center coefficient
laplacian_kernel = np.array([
    [ 0,  1,  0],
    [ 1, -4,  1],
    [ 0,  1,  0]
])

# Apply the Laplacian kernel with a positive center coefficient
opened_image = cv2.filter2D(blurred_image, cv2.CV_64F, laplacian_kernel)

# Display the original image and the opened image
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image (Positive Laplacian)', opened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

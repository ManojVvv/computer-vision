import cv2
import numpy as np

# Load the image
image_path = 'spyder.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to create a blurred version of the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 2)

# Calculate the high-pass image (original image - blurred image)
high_pass_image = cv2.subtract(image, blurred_image)

# Define a scaling factor to control the strength of sharpening
scaling_factor = 1.5

# Combine the high-pass image with the original image using the scaling factor
sharpened_image = cv2.addWeighted(image, 1 + scaling_factor, high_pass_image, -scaling_factor, 0)

# Display the original image, blurred image, high-pass image, and sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('High-Pass Image', high_pass_image)
cv2.imshow('Sharpened Image (Unsharp Masking)', sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
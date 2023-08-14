import cv2
import numpy as np
image_path = 'spyder.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
sharpened_image = image - laplacian
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

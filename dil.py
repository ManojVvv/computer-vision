import cv2
import numpy as np
image_path = 'dhoni.jpeg'
image = cv2.imread(image_path)
original_points = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
transformed_points = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])
perspective_matrix, _ = cv2.findHomography(original_points, transformed_points)
transformed_image = cv2.warpPerspective(image, perspective_matrix, (300, 400))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

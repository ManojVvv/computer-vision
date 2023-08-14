import cv2
import numpy as np
image_path = 'spyder.jpg'
image = cv2.imread(image_path)
original_corners = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
new_width = 300
new_height = 400
new_corners = np.float32([[0, 0], [new_width - 1, 0], [0, new_height - 1], [new_width - 1, new_height - 1]])
homography_matrix, _ = cv2.findHomography(original_corners, new_corners)
transformed_image = cv2.warpPerspective(image, homography_matrix, (new_width, new_height))
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

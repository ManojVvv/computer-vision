import cv2
import numpy as np

# Create a black background
height, width = 480, 640
background = np.zeros((height, width, 3), dtype=np.uint8)

# Calculate the coordinates for the rectangle
rect_width = 200
rect_height = 100
x1 = (width - rect_width) // 2
y1 = (height - rect_height) // 2
x2 = x1 + rect_width
y2 = y1 + rect_height

# Draw the white rectangle on the black background
cv2.rectangle(background, (x1, y1), (x2, y2), (255, 255, 255), -1)

# Display the image
cv2.imshow('Black Background with White Rectangle', background)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image_path = 'kohali.jpeg'
image = cv2.imread(image_path)
x1, y1, x2, y2 = 100, 150, 400, 350
cropped_image = image[y1:y2, x1:x2]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

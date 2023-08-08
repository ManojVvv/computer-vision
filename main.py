import cv2
image = cv2.imread('lion.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Lion', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
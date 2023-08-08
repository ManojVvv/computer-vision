import cv2
import numpy

# read image
src = cv2.imread('lion.jpeg', cv2.IMREAD_UNCHANGED)
# apply guassian blur on src image
dst = cv2.GaussianBlur(src, [3, 3], cv2.BORDER_DEFAULT)
# display input and output image
cv2.imshow("Gaussian Blur",numpy.hstack((src, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
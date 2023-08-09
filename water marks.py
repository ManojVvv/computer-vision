import cv2
import numpy as np
image_path = 'spidy.png.jpg'
watermark_path = 'cap.jpg.jpg'
image = cv2.imread(image_path)
watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
desired_width = 150
watermark_resized = cv2.resize(watermark, (desired_width, int(desired_width * watermark.shape[0] / watermark.shape[1])))
watermark_height, watermark_width, _ = watermark_resized.shape
image_height, image_width, _ = image.shape
position_x = image_width - watermark_width - 10
position_y = image_height - watermark_height - 10
overlay = image.copy()
overlay[position_y:position_y+watermark_height, position_x:position_x+watermark_width] = watermark_resized
alpha = 0.6
watermarked_image = cv2.addWeighted(image, 1, overlay, alpha, 0)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

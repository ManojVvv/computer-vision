import cv2
import numpy as np

def remove_foreground(image_path):
    # Load the image
    image = cv2.imread(image_path)
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define the rectangle enclosing the foreground (you can adjust this based on your image)
    rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)

    # Create initial foreground and background models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Apply GrabCut algorithm
    cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Modify the mask to mark sure background pixels are definite
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Create a new image with the foreground removed
    removed_bg = image * mask2[:, :, np.newaxis]

    return removed_bg, mask2

# Path to the input image
input_image_path = 'spyder.jpg'

# Remove the foreground
removed_bg, foreground_mask = remove_foreground(input_image_path)

# Display the removed foreground image
cv2.imshow('Removed Foreground', removed_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the removed foreground image
cv2.imwrite('removed_foreground.jpg', removed_bg)

# Save the foreground mask
cv2.imwrite('foreground_mask.jpg', foreground_mask * 255)

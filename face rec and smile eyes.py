import cv2

# Load the pre-trained smile detection classifier
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Load the image
image_path = 'kohali.jpeg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect smiles in the image
smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)

# Draw red rectangles around detected smiles
for (sx, sy, sw, sh) in smiles:
    cv2.rectangle(image, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Red rectangle for smiles

# Display the image with rectangles
cv2.imshow('Smile Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

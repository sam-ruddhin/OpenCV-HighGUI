import cv2

# Load an image
image = cv2.imread('wild_animals.jpg')

# Select ROI
roi = cv2.selectROI("Select ROI", image, showCrosshair=True, fromCenter=False)

# Crop the image using the selected ROI
x, y, w, h = roi
cropped_image = image[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Date 19 March: Sobel Filter ->

# It helps detect edges in images by measuring intensity changes.
# It’s useful in object detection, face recognition, medical imaging, etc.

#First we import the OpenCV and Numpy lib
import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE) 

# When we use cv2 IMREAD_GRAYSCALE image will have only one channel (black & white) instead of three (RGB).

# Apply Sobel filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Vertical edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Horizontal edges

#cv2.CV_64F: The data type of the output (float64). This is necessary because edge detection involves subtraction, which can result in negative values.
#ksize=3: Kernel size (must be an odd number, usually 3, 5, or 7).


# Combine both directions
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Show images
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)

# cv2.imshow('Window Name', image_variable) displays images in separate windows.


cv2.waitKey(0)
cv2.destroyAllWindows()

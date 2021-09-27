import cv2 as cv
import numpy as np


img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
#cv.imshow('Makima', img)

blank_img = np.zeros(img.shape[:2], dtype='uint8')

# A color image consists of 3 color channels. We can split an img into their
# own components, meaning we will split the img into its respective channels
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Reconstrcut the img with each of its BGR components.
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# Display each of the colors of the img separately
blue = cv.merge([b, blank_img, blank_img])
cv.imshow('Blue img', blue)

cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
cv.imshow('Makima', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Contours are the the boundaries of objects, they are not the same of edges
# Are useful tools in shape analysis, object detection and object recognition
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#canny = cv.Canny(img, 100, 100)
#cv.imshow('Canny', canny)

# Looks at an image an tries to binarize that img
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# the cv.findContours method looks at the structural element and retourns 2 values
# the contours which is a list of all contours
# hierarchy is the heirarchichal representation
# RETR_LIST returns all the contours
contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} amount of contours in Makima')

# Draw the contours on the blank img
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

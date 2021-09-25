# It is important to note that openCV reads images as BGR (default)
# outside of openCV the RGB format is widespread
# Thus if we try to represent these formats in outside libraries we are going
# to most likely see these images with their colors inverted
import cv2 as cv

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
cv.imshow('Makima', img)

# How to switch between color spaces: rgb, gray, hsv, lav
# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# Convert BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# Convert BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# We can invert any conversion very easily
inverse_rgb = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('RGB TO BGR', inverse_rgb)

cv.waitKey(0)

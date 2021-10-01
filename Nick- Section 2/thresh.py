import cv2 as cv

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
resized = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv.imshow('Makima', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse Simple Thresholding
threshold1, thresh_inverse = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold', thresh_inverse)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 5)
cv.imshow('Adaptive Threhold', adaptive_thresh)

cv.waitKey(0)

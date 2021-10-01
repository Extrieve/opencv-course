import cv2 as cv
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
resized = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv.imshow('Makima', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# Laplacing
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplace', lap)

# Sobel Gradiant Magnitude
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_and(sobelX, sobelY)
cv.imshow('Sobel X', combined_sobel)

# Canny edge comparison
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)

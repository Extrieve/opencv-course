import cv2 as cv
import numpy as np


img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\ciri.jpg')
cv.imshow('Ciri', img)

# Kernel size = rows x cols x (bgr)

# Averaging blurring, we specify a kernel window, and specify pixel intensities
# by averaging surrounding pixels intensities

# Average blue
average = cv.blur(img, (3, 3))
cv.imshow('Avgerage Blur', average)

# Gaussian Blur: each pixel is given a weight, usually less blur than avg
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian', gauss)

# Median blur, similar to avg, but instead of averaging it finds the median.
# Reduces noise in an img.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral blurring: applies blurring but retains the edges of the img
bilateral = cv.bilateralFilter(img, 15, 21, 21)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)

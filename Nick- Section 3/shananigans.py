import cv2 as cv
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\goku.jpg')
cv.imshow('Goky', img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
lap = cv.Laplacian(gray_img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplace', lap)

canny = cv.Canny(gray_img, 100, 125)
cv.imshow('canny', canny)

cv.waitKey(0)

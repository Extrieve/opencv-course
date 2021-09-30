import cv2 as cv
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\jojo.jpg')


newImg = cv.resize(img, (img.shape[1] // 3, img.shape[0] // 3))
cv.imshow('Jojo', newImg)

blank = np.zeros(newImg.shape[:2], dtype='uint8')
#cv.imshow('Blank Img', blank)

circle = cv.circle(
    blank, (newImg.shape[1] // 2 + 20, newImg.shape[0] // 2 - 250), 150, 255, -1)

# Create our masked img
masked = cv.bitwise_and(newImg, newImg, mask=circle)
cv.imshow('Masked Img', masked)

cv.waitKey(0)

import cv2 as cv
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')

cv.imshow('Makima', img)


# Translations
# negative x values are going to shift the img to the left
# negative y values are going to shift the image upwards
def translate(img, x, y):
    # Represent the img in a translation matrix.
    trans_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, trans_matrix, dimensions)


translated_img = translate(img, -100, 200)
cv.imshow('Translated', translated_img)


# img rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_matrix, dimensions)


rotated = rotate(img, 90)
cv.imshow('Rotated', rotated)


# Resizing
resized = cv.resize(
    img, (img.shape[1] // 2, img.shape[0] // 2), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


# Flip an image
flip = cv.flip(resized, -1)
cv.imshow('Vertical Flip', flip)

cv.waitKey(0)

import cv2 as cv

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')

cv.imshow('Makima', img)

# Converting an img to grayscale, to see the intesity distribution of pixels.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur / gausian blur / ksize has to be odd
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

# How to dilate an image using a structural element
dilated = cv.dilate(canny, (3, 3), iterations=1)
#cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
#cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resized)

# Cropping, basically array slicing
cropped = img[800:1200, 200:800]
cv.imshow('Bewbs', cropped)

cv.waitKey(0)

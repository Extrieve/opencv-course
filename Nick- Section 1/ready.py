import cv2 as cv

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\cat_large.jpg')

# Display the img
cv.imshow('Cat', img)

# Add a delay, 0 is infinite amount of time.
cv.waitKey(0)

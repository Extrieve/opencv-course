import cv2 as cv
import numpy as np

# Create a blank image using numpy
blank = np.zeros((500, 500, 3), dtype='uint8')

# 1. Painting the img to a certain color.
#blank[::] = 0, 255, 255

# Draw a rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)

# Draw a cirlce.
cv.circle(blank, (blank.shape[1] // 2,
          blank.shape[0] // 2), 30, (0, 0, 255), thickness=-1)

# Draw a line.
cv.line(blank, (0, 0), (blank.shape[1] // 2,
        blank.shape[0] // 2), (255, 0, 0), thickness=4)

#How to write text on an img.
cv.putText(blank, 'Hello Sucka', (255, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
# Display the img
cv.imshow('circle', blank)

cv.waitKey(0)

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\makima.jpg')
resized = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv.imshow('Makima', resized)

blank = np.zeros(resized.shape[:2], dtype='uint8')
circle = cv.circle(
    blank, (resized.shape[1] // 2, resized.shape[0] // 2), 100, 255, -1)


# Compute histogram for grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
masked = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', masked)

gray_histogram = cv.calcHist([gray], [0], masked, [256], [0, 256])


# Display it with matlplotlib
plt.figure()
plt.title('Grayscale Historgram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_histogram)
plt.xlim([0, 256])
plt.show()

# Color histogram
masked = cv.bitwise_and(resized, resized, mask=circle)
cv.imshow('Mask', masked)

plt.figure()
plt.title('Color Historgram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    histogram = cv.calcHist([resized], [i], None, [256], [0, 256])
    plt.plot(histogram, color=col)
    plt.xlim([0, 256])

plt.show()


cv.waitKey(0)

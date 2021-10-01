import cv2 as cv

img = cv.imread(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Photos\group 1.jpg')
cv.imshow('Lady Face', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Read and assign the XML file to our variable
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))

cv.imshow('Detected Faces', img)

cv.waitKey(0)

import os
import cv2 as cv
import numpy as np

people = []

for item in os.listdir(r'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Faces\train'):
    people.append(item)

print(people)
DIR = r'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Faces\train'

features = []
labels = []

haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=1)

            for(x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+h]
                features.append(faces_roi)
                labels.append(label)


create_train()
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

# Transform the list into numpy arrays for better performance
features = np.array(features, dtype='object')
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the face recognizer with the features and label list
face_recognizer.train(features, labels)
print('Training Concluded')

# save the model and recognizer
face_recognizer.save('faces_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)

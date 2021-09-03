import cv2 as cv

# Reading Videos. Input an integer with an integer.
capture = cv.VideoCapture(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Videos\dog.mp4')

# For videos we need to use an inifite loop to read the video frame by frame.
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # Stop the loop when we run out of frames.
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

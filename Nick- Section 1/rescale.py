import cv2 as cv

# Rescaling images with a function


def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


def rescale_frame(frame, scale=0.75):
    # For imgs, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(
    'D:\Documents\OneDrive - University of South Florida\Python\OpenCV Tutorial\opencv-course\Resources\Videos\dog.mp4')

# For videos we need to use an inifite loop to read the video frame by frame.
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)
    cv.imshow('Video', frame_resized)

    # Stop the loop when we run out of frames.
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# Add a delay, 0 is infinite amount of time.
cv.waitKey(0)

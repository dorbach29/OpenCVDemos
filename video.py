import numpy as numpy
import cv2

#INITIALIZATION
cap = cv2.VideoCapture('SpanishVid.mp4')


fps = cap.get(cv2.CAP_PROP_FPS)
waitTime = int(100 / fps)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

while(True):
    #Getting the frame 
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', frame)
    if cv2.waitKey(waitTime) > 0:
        ord()
        break
cap.release()
cv2.destroyAllWindows() 
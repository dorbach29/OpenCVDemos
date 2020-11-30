import numpy as np 
import cv2

#Showin Message
img = cv2.imread('message.png' , 0)
cv2.imshow('Hello' , img)

 #Waiting for keystroke then displaying message 
key = cv2.waitKey(0) - 48
cv2.destroyAllWindows()
image = str(key) +'.png'

if (key > 3 or key < 1):
    image = 'Error.png'


img = cv2.imread(image, 1)
cv2.imshow('Bob' , img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

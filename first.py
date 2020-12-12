import numpy as np 
import cv2
import time 
import random as r

#Getting Image
img = cv2.imread('Spiral.jpg' , 1)

#Resizing Image
scale_percent = 3
width = int(img.shape[1] * scale_percent)
height = int(img.shape[0] * scale_percent)
dim = (width, height)
img = cv2.resize(img, dim, 0, cv2.INTER_CUBIC)




#Looping through changing animation until user wants to stop
timeElapsed = 0
while(True): 
    
    
    if(timeElapsed % 8 == 0):
        scale_percent = 1.1
        width = int(img.shape[1] * scale_percent)
        height = int(img.shape[0] * scale_percent)
        dim = (width, height)
        img = cv2.resize(img, dim, 0, cv2.INTER_CUBIC)
    
    
    #Zooming in on one point in the spiral by moving 10 pixels each on each side
    rows, cols, ch = img.shape
    pts1 = np.float32([[10, 10], [cols - 10, 10], [10, rows - 10], [rows - 10, cols - 10]])
    pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [rows, cols]])
    Matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, Matrix, (cols, rows))

    #Making random squares of the image shift to new locations
    numSquares = r.randint(1, 3)
    for i in range(numSquares):
        squareSize = r.randint(1, 100)
        squarePos = r.randint(0, rows - squareSize)
        squarePos2 = r.randint(0, rows - squareSize)
        squarePos3 = r.randint(0, rows - squareSize)
        square = img[squarePos:squarePos + squareSize, squarePos:squarePos + squareSize ]
        img[squarePos2:squarePos2 + squareSize, squarePos3:squarePos3 + squareSize ] = square 

    if(timeElapsed == 50):
        timeElapsed = 0

        #Getting Image
        img = cv2.imread('Spiral.jpg' , 1)

        #Resizing Image
        scale_percent = 3
        width = int(img.shape[1] * scale_percent)
        height = int(img.shape[0] * scale_percent)
        dim = (width, height)
        img = cv2.resize(img, dim, 0, cv2.INTER_CUBIC)

    cv2.imshow('Hello' , img)
    keyPressed = cv2.waitKey(50)
    timeElapsed += 1
    print(timeElapsed)
    if(keyPressed != -1):
        cv2.destroyAllWindows()
        break


import cv2 as cv
import numpy as np

black = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Black', black)

#1.Paint the image a certain color
black[100:200, 300:400] = [0, 0, 255]
cv.imshow('Red', black)

#2.Draw a Rectangle
cv.rectangle(black, (0,0), (250,250), (0,250,0), thickness= 2)
cv.imshow('Rectangle', black)  

#3.Draw a Circle
cv.circle(black, (black.shape[1]//2, black.shape[0]//2), 40, (0,0,255), thickness= -1)
cv.imshow('Circle', black)

#4.Draw a line
cv.line(black, (0,0), (black.shape[1]//2, black.shape[0]//2), (255,0,0), thickness= 2)
cv.imshow('Line', black)

#5.Write text
cv.putText(black, 'Hello', (255,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), thickness= 2)
cv.imshow("Text", black)


cv.waitKey(0)

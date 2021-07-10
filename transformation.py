import cv2 as cv
import numpy as np

img = cv.imread('tree_home.jpg')
img = cv.resize(img, (720, 480), interpolation= cv.INTER_AREA)

cv.imshow('Img', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([1,0,x],[0,1,y])  

# Rotation


# Flip
flip = cv.flip(img, 1)   # 0:對x軸向上flip ; 1:對y軸向右flip
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
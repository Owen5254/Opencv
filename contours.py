import cv2 as cv
import numpy as np

img = cv.imread('tree_home.jpg')
img = cv.resize(img, (720, 480), interpolation= cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Find how many contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} is founded!')

# Draw the contours
black = np.zeros(img.shape, dtype= 'uint8')
cv.drawContours(black, contours, -1, (0,0,255), 1)  # 第三個元素為畫幾條線,-1 means all the lines
cv.imshow('Contours_Drawn', black)

# Binarize
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread('tree_home.jpg')
img = cv.resize(img, (720,480), interpolation= cv.INTER_AREA)
cv.imshow('Img', img)

b, g, r= cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

blank = np.zeros(img.shape[0:2], dtype= np.uint8)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('M_Blue', blue)
cv.imshow('M_Green', green)
cv.imshow('M_Red', red)
 
cv.waitKey(0)
import cv2 as cv

img= cv.imread('tree_home.jpg')
img= cv.resize(img, (720,480), interpolation= cv.INTER_AREA)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)   
cv.imshow('Simple Thresholding', thresh)

threshold, thresh_inverse= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inverse)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 1)
cv.imshow('Adapting Thresholding', adaptive_thresh)


cv.waitKey(0)
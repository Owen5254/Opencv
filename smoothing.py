import cv2 as cv

img = cv.imread('tree_home.jpg')
img = cv.resize(img, (720,480), interpolation= cv.INTER_AREA)
cv.imshow('Img', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Guassian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Guassian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Medain Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)
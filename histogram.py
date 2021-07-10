import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('tree_home.jpg')
img = cv.resize(img, (720,480), interpolation= cv.INTER_AREA)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[0:2], dtype= 'uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('Masked_Gray', mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram') 
plt.xlabel('Bins')
plt.ylabel('# of pixel')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# Color Histogram
color= ('b', 'g', 'r')
for i,col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color= col)
    plt.xlim([0,256])
plt.show()
 

cv.waitKey(0) 
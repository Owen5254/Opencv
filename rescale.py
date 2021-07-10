import cv2 as cv

img = cv.imread('tree_home.jpg')
cv.imshow('img',img)

def rescaleFrame(frame, scale= 0.2):
    width = int(frame.shape[1] * scale)   # 1是寬的代號
    height = int(frame.shape[0] * scale)  # 0是長的代號
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
  
    
img_resize = rescaleFrame(img)
cv.imshow('img_resized', img_resize)

cv.waitKey(0)


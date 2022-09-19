import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

img = cv.imread('data/Track 10-22/60_4.png',0)
print(cv.THRESH_BINARY,cv.THRESH_OTSU)
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imwrite('60_4_otsu.png',th3)
print("done")

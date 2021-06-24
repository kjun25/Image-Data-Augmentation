import cv2
import numpy as np
image = cv2.imread('F:/kjYun/2021/imgaug/ongsim2.jpg')

cv2.imshow('Source', image)

dst = cv2.medianBlur(image, 3)
cv2.imshow('medianBlur3', dst)

dst2 = cv2.medianBlur(image, 5)
cv2.imshow('medianBlur5', dst2)

dst3 = cv2.medianBlur(image, 7)
cv2.imshow('medianBlur7', dst3)

dst4 = cv2.medianBlur(image, 9)
cv2.imshow('medianBlur9', dst4)

cv2.waitKey()
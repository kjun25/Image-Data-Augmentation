import cv2
import numpy as np
image = cv2.imread('F:/kjYun/2021/imgaug/ongsim2.jpg')

cv2.imshow('Source', image)

dst = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow('gaussianBlur3', dst)

dst2 = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('gaussianBlur5', dst2)

dst3 = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('gaussianBlur7', dst3)

dst4 = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow('gaussianBlur9', dst4)

cv2.waitKey()
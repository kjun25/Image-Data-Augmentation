import cv2
import numpy as np
image = cv2.imread('F:/kjYun/2021/imgaug/ongsim2.jpg')

rows, cols = image.shape[:2]

low_pass_filter_3x3 = np.ones((3, 3), np.float32) / 9.0
blurring_3 = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
low_pass_filter_5x5 = np.ones((5, 5), np.float32) / 25.0
blurring_5 = np.array([[1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25], [1 / 25, 1 / 25, 1 / 25, 1 / 25, 1 / 25]])
low_pass_filter_7x7 = np.ones((7, 7), np.float32) / 49.0
low_pass_filter_9x9 = np.ones((9, 9), np.float32) / 81.0

cv2.imshow('Source', image)

dst = cv2.filter2D(image, -1, low_pass_filter_3x3)
cv2.imshow('low_pass_filter_3x3', dst)
#cv2.imwrite("blurredImage_3x3.jpg", dst)

dst2 = cv2.filter2D(image, -1, low_pass_filter_5x5)
cv2.imshow('low_pass_filter_5x5', dst2)
#cv2.imwrite("blurredImage_5x5.jpg", dst2)

dst3 = cv2.filter2D(image, -1, low_pass_filter_7x7)
cv2.imshow('low_pass_filter_7x7', dst3)
#cv2.imwrite("blurredImage_7x7.jpg", dst3)

dst4 = cv2.filter2D(image, -1, low_pass_filter_9x9)
cv2.imshow('low_pass_filter_9x9', dst4)
#cv2.imwrite("blurredImage_9x9.jpg", dst4)

cv2.waitKey()

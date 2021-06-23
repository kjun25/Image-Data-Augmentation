import numpy as np
import cv2

src = cv2.imread('F:/kjYun/2021/imgaug/ongsim2.jpg', cv2.IMREAD_COLOR)

sharpening_1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpening_2 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

cv2.imshow('src', src)
Sharpening1 = cv2.filter2D(src, -1, sharpening_1)
cv2.imshow('Sharpening5', Sharpening1)
#cv2.imwrite("F:/kjYun/2021/imgaug/sharpening5Image.jpg", add)
Sharpening2 = cv2.filter2D(src, -1, sharpening_2)
cv2.imshow('Sharpening9', Sharpening2)
#cv2.imwrite("F:/kjYun/2021/imgaug/sharpening9Image.jpg", add)

cv2.waitKey()
cv2.destroyAllWindows()

import numpy as np
import cv2

src = cv2.imread('F:/kjYun/2021/imgaug/ongsim2.jpg', cv2.IMREAD_COLOR)

val = 45
array = np.full(src.shape, (val, val, val), dtype=np.uint8)

add = cv2.add(src, array)
sub = cv2.subtract(src, array)

cv2.imshow('src', src)
cv2.imshow('add', add)
#cv2.imwrite("F:/kjYun/2021/imgaug/addImage.jpg", add)
cv2.imshow('sub', sub)
#cv2.imwrite("F:/kjYun/2021/imgaug/subImage.jpg", sub)

cv2.waitKey()
cv2.destroyAllWindows()

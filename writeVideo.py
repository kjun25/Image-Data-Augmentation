import numpy as np
import cv2

cap = cv2.VideoCapture('F:/kjYun/2021/imgaug/ongsim3.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('F:/kjYun/2021/imgaug/ongsim3.mp4', fourcc, 29.970, (1920,1080))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        val = 30
        array = np.full(frame.shape, (val, val, val), dtype=np.uint8)
        sharpening_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        size = 30

        motion_blur = np.zeros((size, size))
        motion_blur[int((size - 1) / 2), :] = np.ones(size)
        motion_blur = motion_blur / size

        sub = cv2.subtract(frame, array)
        Sharpening = cv2.filter2D(sub, -1, sharpening_1)
        blurResult = cv2.medianBlur(Sharpening, 3)
        dst = cv2.filter2D(blurResult, -1, motion_blur)
        out.write(dst)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
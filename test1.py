import cv2
import numpy as np
img = cv2.imread("123.PNG", 0)  #0為黑白,1為彩色
print(img)
cv2.namedWindow("123", cv2.WINDOW_NORMAL)
cv2.imshow("123", img)
cv2.imwrite("123test.PNG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
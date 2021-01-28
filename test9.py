import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("123.PNG", 1)  #0為黑白,1為彩色
b = cv2.imread("123.PNG", 1)
img1 = b[200:400, 200:400]
img2 = b[300:500, 400:600]
print(img1)
print(img2)
dst=cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
b[300:500, 400:600] = dst

cv2.namedWindow("123", cv2.WINDOW_NORMAL) #調整影像大小
cv2.imshow("123", img) #顯示影像
cv2.imshow("b", b)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("123.PNG", 1)  #0為黑白,1為彩色
b = cv2.imread("123.PNG", 1)
b[100:200,100:200,0]=0
b[300:500,600:800,1]=0
b[500:600,300:500,2]=0
print(b)

cv2.namedWindow("123", cv2.WINDOW_NORMAL) #調整影像大小
cv2.imshow("br", img) #顯示影像
cv2.waitKey(0) 
cv2.destroyAllWindows() 
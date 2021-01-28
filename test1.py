import cv2
import numpy as np
img = cv2.imread("123.PNG", 0)  #0為黑白,1為彩色
print(img) #印出RGB
cv2.namedWindow("123", cv2.WINDOW_NORMAL) #調整影像大小
cv2.imshow("123", img) #顯示影像
cv2.imwrite("123test.PNG", img) #另存圖片檔名
cv2.waitKey(0) 
cv2.destroyAllWindows() 
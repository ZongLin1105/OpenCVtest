import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("123.PNG", 1)  #0為黑白,1為彩色
img[100, 100] = [0, 0, 0]
print(img.shape, img.size)
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #顏色轉換方式
roi = img[430:470, 600:730]  #600:730, 430:470
img[300:340, 530:660]=roi #530:660, 300:340
plt.imshow(img1)  
plt.xticks([]), plt.yticks([]) #影像顯示座標值
plt.show()

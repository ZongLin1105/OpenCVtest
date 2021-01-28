import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("123.PNG", 1)  #0為黑白,1為彩色

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #顏色轉換方式

print(img) #印出RGB
plt.imshow(img1)  
plt.xticks([]), plt.yticks([]) #影像顯示座標值
plt.show()

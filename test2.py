import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("123.PNG", 0)  #0為黑白,1為彩色
print(img) #印出RGB
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) 
plt.show()

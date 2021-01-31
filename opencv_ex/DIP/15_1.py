import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/test11.jpg', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  #>127要 <127不要
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) #低於閥值黑色,高於閥值正常
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray') #2*3
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

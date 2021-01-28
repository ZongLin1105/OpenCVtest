import cv2
import numpy as np

img=np.zeros((512,512,3), np.uint8) #產生np圖檔,np.uint8只有連到255

#Import only if not previously imported
# Coordinates must be a tuple - (x,y)
cv2.line(img,(0,0),(500,500),(0,255,255),5) #畫線
cv2.rectangle(img,(100,100), (300,300), (255, 0, 255) ,3) #畫正方形                 
cv2.circle(img,(200,200), 150, (133, 133, 133) , 4)  #畫圓
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)  #畫橢圓
font = cv2.FONT_HERSHEY_SIMPLEX #新增文字
cv2.putText(img, "test", (200, 200),font, 2, (255, 255, 255),5) #新增文字

points = np.array([[200, 200], [300, 100], [400, 200], [400, 400], [200, 400]], np.int32) #畫多邊形
print(points)
cv2.polylines(img,[points], True, (200,200,200), 3)   #畫多邊形,True、1為封閉區間               


cv2.imshow("Window Name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
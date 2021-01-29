import cv2
import numpy as np
cap=cv2.VideoCapture(0) #放想處理的影像檔
while(1):
# 獲取每一帧；判斷有沒有開狀態
    ret,frame=cap.read() 
# 轉换到 HSV；BGR轉換HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# 設定蓝色的侷值;設定HSV藍色的值
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])




# 根据侷值构建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
# 对原图像和掩模進行位運算
    res=cv2.bitwise_and(frame,frame,mask=mask)
# 显示图像;有雜訊表示有光線打到
    cv2.imshow('frame',frame) #原圖
    cv2.imshow('mask',mask) #mask圖
    cv2.imshow('res',res) #遮蔽圖
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关閉窗口
cv2.destroyAllWindows()

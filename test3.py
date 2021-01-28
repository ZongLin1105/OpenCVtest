import cv2
import numpy as np
#Import only if not previously imported
import cv2
# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('testoutput.avi',fourcc, 30, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
write.release()
cv2.destroyAllWindows()


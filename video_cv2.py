import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cv2
import numpy as np
i = 0
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1
    if cv2.waitKey(5000) & 0xFF == ord('q'):
        
        break

cap.release()

cv2.destroyAllWindows()
from tempfile import NamedTemporaryFile
import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cv2
import numpy as np

from vision import prediction
i = 0
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    file = NamedTemporaryFile(suffix=".jpg",prefix="./frame_",delete=True)
    cv2.imwrite(file.name, frame)
    ret = prediction(file.name)
    print(ret)
    file.close()
    i += 1
    if cv2.waitKey(2000) & 0xFF == ord('q'):
        
        break

cap.release()

cv2.destroyAllWindows()
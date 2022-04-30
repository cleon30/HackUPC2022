from tempfile import NamedTemporaryFile
import pydrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cv2
import numpy as np
from details import details
from detection import detection_object

from vision import prediction
i = 0
cap = cv2.VideoCapture(0)

while(True):
    dictionary = {}
    ret, frame = cap.read()
    object = detection_object(frame)
    cv2.imshow('frame',frame)
    file = NamedTemporaryFile(suffix=".jpg",prefix="./frame_",delete=True)
    cv2.imwrite(file.name, frame)
    ret = prediction(file.name)
    dictionary['room'] = ret[0]; dictionary['score'] = ret[1] ; dictionary['objects'] = object
    print(ret, object)
    file.close()
    i += 1
    if cv2.waitKey(2000) & 0xFF == ord('q'):
        
        break

cap.release()

cv2.destroyAllWindows()
import cv2
def detection_object(img):
    #img = cv2.imread('image2.png')
    c = []
    with open('coco.names', 'r') as f:
        classes = f.read().splitlines()
    
    net = cv2.dnn.readNetFromDarknet('yolov4.cfg', 'yolov4.weights')
    
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    
    classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)
    
    for (classId, score, box) in zip(classIds, scores, boxes):
    
        c.append(classes[classId])
    return c
    
    

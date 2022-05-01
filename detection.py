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
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
        c.append(classes[classId])


        text = '%s: %.2f' % (classes[classId], score)
        cv2.putText(img, text, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    color=(0, 255, 0), thickness=2)
    return c
    
    

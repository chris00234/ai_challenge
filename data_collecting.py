from ultralytics import YOLO

import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

import uuid # unique identifier
import os
import time

IMAGES_PATH = os.path.join('data','images')
labels = ['awake', 'drowsy']
number_imgs = 20

cap = cv2.VideoCapture(0)

# Loop through labels
for label in labels:
    
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    
    # loop through image range
    for img_num in range(number_imgs):
        
        print('collecting images for {}, image number {}'.format(label, img_num))
        
        ret, frame = cap.read()
        
        imgname = os.path.join(IMAGES_PATH, label + '.'+str(uuid.uuid1()) +'.jpg')
        
        cv2.imwrite(imgname, frame)
        cv2.imshow('Image collection', frame)
        
        time.sleep(2)
    
    if cv2.waitKey(10) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
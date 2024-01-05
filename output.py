from ultralytics import YOLO

import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

model_path = os.path.join('.', 'runs', 'detect', 'train3', 'weights', 'last.pt')
model = YOLO(model_path)
results = model.predict(source = "0", show = True)
print(results)
from ultralytics import YOLO

import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

model = YOLO("yolov8s.pt")
model.train(data = "dataset.yaml", epochs= 5)
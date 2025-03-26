import pandas as pd 
from ultralytics import YOLO
import os

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # "yolov8n.pt" is the smallest & fastest model

# Train the model on your dataset using CPU
model.train(data="D:\#Safety Kit\Construction-Site-Safety-PPE-Detection\data\data.yaml", epochs=100, imgsz=640, device="cpu")  # 👈 Use "cpu"


# Load the trained model
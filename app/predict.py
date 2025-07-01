# Prediction logic
 
from utils import preprocess_image
from ultralytics import YOLO


def predict(image_path):
    preprocessed_image = preprocess_image(image_path)

    model= YOLO("weight/last.pt")
    predictions = model.predict(source=preprocess_image, imgsz=224,conf=0.1)
    return predictions
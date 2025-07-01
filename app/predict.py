# Prediction logic

from model import load_model
from utils import preprocess_image
from ultralytics import YOLO


def predict(image_path):
    preprocessed_image = preprocess_image(image_path)

    model= load_model()
    predictions = model.predict(source=preprocessed_image, imgsz=224,conf=0.1)
    return predictions


def predict_stream(image_stream):
    pass


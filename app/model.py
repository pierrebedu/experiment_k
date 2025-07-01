# Model training and loading
import os

def train_model():
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    model.train(data="../data/data.yaml", epochs=200, imgsz=224, batch=16)
    model.save("../weights/last.pt")


def load_model():
    if not os.path.exists("../weights/last.pt"):
        raise FileNotFoundError("Weight file not found. Please train the model first.")
    from ultralytics import YOLO
    model = YOLO("../weights/last.pt")
    return model


if __name__ == "__main__":
    train_model()
    print("Model trained successfully.")

# Model training and loading
import os

def train_model():
    from ultralytics import YOLO
    model = YOLO("yolov8m.pt")
    model.train(data="../data/data.yaml", epochs=200, imgsz=224, batch=16)
    model.save("weights/last.pt")


def load_model():

    import glob

    matches = glob.glob('**/weights/last.pt', recursive=True)
    if not matches:
        raise FileNotFoundError("Weight file not found. Please train the model first.")
    else:
        weights_path = matches[0]
        from ultralytics import YOLO
        model = YOLO(weights_path)
        return model

if __name__ == "__main__":
    train_model()
    print("Model trained successfully.")

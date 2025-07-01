# Model training and loading

def train_model():

    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    model.train(data="data/data.yaml", epochs=30, imgsz=224, batch=16)
    model.save("weight/last.pt")


def load_model():
    # return error if weight file does not exist
    if not os.path.exists("weight/last.pt"):
        raise FileNotFoundError("Weight file not found. Please train the model first.")
    from ultralytics import YOLO
    model = YOLO("weight/last.pt")
    return model

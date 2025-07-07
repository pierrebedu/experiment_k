def retrain(yaml_file_path):
    from ultralytics import YOLO
    model = YOLO("yolov8m.pt")
    model.train(data=yaml_file_path, epochs=200, imgsz=224, batch=16)
    model.save("weights/last.pt")

if __name__ == "__main__":
    retrain("../data/data.yaml")
    print("Model retrained successfully.")
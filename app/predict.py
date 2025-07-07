# Prediction logic
import cv2
from model import load_model

def predict_fct(image_path):
    model= load_model()
    predictions = model.predict(source=image_path, imgsz=224,conf=0.4)
    return predictions

def visualize(image_path):
    pred=predict_fct(image_path)
    boxes=pred[0].boxes

    im=cv2.imread(image_path)
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        label = int(box.cls[0].item())
        label = "pen" if label == 2 else "kit" 
        color = (0, 0, 255) if label == "kit" else (0, 255, 0)  
        cv2.rectangle(im, (x1, y1), (x2, y2), color, 2)
        cv2.putText(im, str(label), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.imwrite("visualize_result.jpg", im)
    

def infere_vid(video_path):
    model= load_model()
    model.predict(source=video_path, imgsz=224,conf=0.4, save=True)

def predict_stream():
    from ultralytics import YOLO
    model = YOLO("weights/last.pt")
    model.predict(source=0, device="cpu", show=True, conf=0.7, imgsz=224, iou=0.5)

if __name__ == "__main__":
    #path="test_image.jpg"
    #pred= predict_fct(path)
    #print(pred[0].boxes.xywh)
    #visualize(path)

    predict_stream()

# FastAPI entry point
from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from predict import predict_fct
from camera import capture_image
import cv2

app = FastAPI()

@app.post("/predict/")
async def predict_image(
    use_camera: bool = Form(False),
    file: Optional[UploadFile] = File(None)
):
    try:
        if use_camera:
            frame = capture_image()
            image_path = "realtime_image.jpg"
            cv2.imwrite(image_path, frame)
        else:
            if file is None:
                return {"error": "No file uploaded and use_camera is False"}
            image_path = file.filename
       
        pred = predict_fct(image_path)
        predictions_list = []
        for box in pred[0].boxes.xywh:
            predictions_list.append({
                "x_center": box[0].item(),
                "y_center": box[1].item(),
                "width": box[2].item(),
                "height": box[3].item(),
            })

        return {"predictions": predictions_list}

    except Exception as e:
        print("Erreur dans /predict/:", e)
        return {"error": str(e)}


@app.get("/healthcheck/")
async def healthcheck():
    try:
        import os
        import random
        import glob
        data_folder = "/home/pierre/experiment_k/data/train/images/"
        if not os.path.exists(data_folder):
            return {"status": "error", "message": "Data folder does not exist."}
        jpg_files = glob.glob(os.path.join(data_folder, "*.jpg"))
        if not jpg_files:
            return {"status": "error", "message": "No JPG files found in /data folder."}
        random_image = random.choice(jpg_files)
        predict_fct(random_image)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "ok"}



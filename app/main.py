# FastAPI entry point
 
from fastapi import FastAPI, File, UploadFile
from predict import predict_fct
from camera import capture_image
import cv2

app = FastAPI()

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try :
        image_path = f"{file.filename}"
        pred = predict_fct(image_path)
        predictions_list = []
        for box in pred[0].boxes.xywh:
            predictions_list.append({
                "x_center": box[0].item(),
                "y_center": box[1].item(),
                "width": box[2].item(),
                "height": box[3].item(),
            })

        return {"predictions ": predictions_list}
    
    except Exception as e:
        print("Erreur dans /predict/:", e)
        return {"error": str(e)}


@app.get("/healthcheck/")
async def healthcheck():
    try:
        import os
        import random
        import glob
        data_folder = "/home/pbedu/experiment_k/data/train/images"
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


@app.post("/predict_realtime/")
async def predict_realtime():
    try :
        frame=capture_image()  # Assuming this function captures an image and saves it to a predefined path
        #save frame on disk
        cv2.imwrite("realtime_image.jpg", frame)
        pred = predict_fct("realtime_image.jpg")
        predictions_list = []
        for box in pred[0].boxes.xywh:
            predictions_list.append({
                "x_center": box[0].item(),
                "y_center": box[1].item(),
                "width": box[2].item(),
                "height": box[3].item(),
            })

        return {"predictions ": predictions_list}
    
    except Exception as e:
        print("Erreur dans /predict/:", e)
        return {"error": str(e)}

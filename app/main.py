# FastAPI entry point

from fastapi import FastAPI, UploadFile, File, Form, Request, Response
from typing import Optional
from predict import predict_fct
from camera import capture_image
import cv2
import logging
from starlette.background import BackgroundTask

app = FastAPI()

@app.post("/predict/")
async def predict_image(
    use_camera: bool = Form(False),
    file: Optional[UploadFile] = File(None)
):
    try:
        if use_camera:
            frame = capture_image()
            cv2.imwrite("realtime_image.jpg", frame)
            image_path = "realtime_image.jpg"
        else:
            if file is None:
                return {"error": "No file uploaded and use_camera is False"}
            image_path = f"/tmp/{file.filename}"
            with open(image_path, "wb") as f:
                f.write(await file.read())
       
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


logging.basicConfig(filename="info.log", level=logging.INFO)

def log_info(method, url_path, req_body, res_body):
    logging.info(f"API called: {method} {url_path}")
    logging.info(f"Request body: {req_body}")
    logging.info(f"Response body: {res_body}")


@app.middleware("http")
async def log_request_response(request: Request, call_next):
    req_body = await request.body()
    response = await call_next(request)

    # Read response body (works for JSON/text responses)
    chunks = []
    async for chunk in response.body_iterator:
        chunks.append(chunk)
    res_body = b"".join(chunks)

    # Log method and path along with bodies
    task = BackgroundTask(
        log_info,
        request.method,
        request.url.path,
        req_body,
        res_body
    )
    return Response(
        content=res_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
        background=task
    )

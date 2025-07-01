# FastAPI entry point
 
from fastapi import FastAPI, File, UploadFile
from app.predict import predict  

app = FastAPI()

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    image_path = f"/tmp/{file.filename}"
    with open(image_path, "wb") as f:
        f.write(await file.read())
    
    predictions = predict(image_path)
    
    return {"predictions :", predictions}


@app.get("/healthcheck/")
async def healthcheck():
    try:
        import os
        import random
        import glob
        data_folder = "/data"
        jpg_files = glob.glob(os.path.join(data_folder, "*.jpg"))
        if not jpg_files:
            return {"status": "error", "message": "No JPG files found in /data folder."}
        random_image = random.choice(jpg_files)
        predict(random_image)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    return {"status": "ok"}
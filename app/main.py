from fastapi import FastAPI, File, UploadFile
from model import predict  

app = FastAPI()

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    image_path = f"/tmp/{file.filename}"
    with open(image_path, "wb") as f:
        f.write(await file.read())
    
    predictions = predict(image_path)
    
    return {"predictions :", predictions}
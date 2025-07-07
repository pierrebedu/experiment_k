## Computer vision with camera and apis


# Constraints /choices:
- choice of a use case close to your problematics : wanted to segment things like a pen or a pipette, but data annotation would have taken too long
- object detection paradigm was doable within a week
- can be run in real time on cpu
- CNNs are SOTA for most computer vision tasks

# Dataset :
- pen and kit images
- home made with a few personnal tricks to accelerate the process
- video filmed then automatic extraction of 3 images per second.
- hand labbeling of a few samples then proposals given by roboflow annotate

# Steps to run the API (uvicorn, etc.)
- launch a server : \
`uvicorn main:app --reload --port 8000  --log-level debug`
- check health with : \
`curl http://127.0.0.1:8000/healthcheck/`


# Example API call
- call with a test image : \
`curl 'http://127.0.0.1:8000/predict/' -F 'file=@/home/pierre/experiment_k/app/test_image.jpg'`
- image caught on demand by usb camera : \
`curl  http://127.0.0.1:8000/predict/ -F "use_camera=true" `


# docker
- build 
`docker build -t mon-fastapi-app .  `
- run
`docker run  -p 8000:8000 --name conteneur_pierre  mon-fastapi-app   `
 - request
`curl   'http://127.0.0.1:8000/predict/'   -F 'file=@app/test_image.jpg' `


# code structure
experiment_k/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── camera.py        # Simulated camera module
│   ├── model.py         # Model training and loading
│   ├── predict.py       # Prediction logic
│   └── utils.py         # useless here
│
├── data/                # Dataset (optional if downloaded)
├── requirements.txt
└── README.md

See requirements for python installation. Any Python >3.6 should be fine.

# Additional features :
- realtime prediction
- one unit test to demonstrate
- retrain with "python retrain.py"
- logging of APIs



# To improve :
- robustify
- systematic unit tests

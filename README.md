## Computer vision with camera and apis


# Constraints /choices:
- choice of an app that could answer to your need : wanted to segment things like a pen or a pipette bur data annotation would have taken too much time
- object detection paradigm was doable
- can be run in real time on cpu
- CNN are SOTA for most computer vision tasks

# Dataset :
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
- image caught on demand by camera : \
`curl -F "use_camera=true" http://127.0.0.1:8000/predict/`


# docker
docker build -t mon-fastapi-app .  # reads the dockerfile in which there isa CMD [uvicorn, etc ...] and creates iamge. builds web service.
docker run --gpus all -p 8000:8000 --name conteneur_pierre  mon-fastapi-app -d  #creates and activates contener. -d for detaching app from terminal. (attach attach a volume if files sharing is needed)

docker run -p 8000:8000 mon-fastapi-app


curl -X 'POST'   'http://127.0.0.1:8000/predict/'   -F 'file=@images/defaut_blanc.jpg' #interoger l'api dans le terminal


# Additional features :
- one unit test to demonstrate
- retrain with "python retrain.py"
- logging of APIs





TO DO :
- robustify (camera fails. image does not exist.)
- systematic unit tests
- docker



prioritize:
docker
realtime prediction
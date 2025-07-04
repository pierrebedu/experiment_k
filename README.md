## Computer vision with camera and apis


# Constraints /choices:
- wanted to segment things like a pen or a pipette bur data annotation would have taken too much time
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



# Additional features :
- one unit test to demonstrate
- retrain with "python retrain.py"





TO DO :
- robustify
- systematic unit tests
- docker
- logs requests and responses


prioritize:
docker
logging calls
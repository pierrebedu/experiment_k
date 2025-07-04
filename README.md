# experiment_k
personnal camera tests

# Constraints /choices:
- could be close to real problematic (- segmentation task : costly to have labelled data, detection task is easier)
- real time on cpu
- sota

# Dataset :
- home made
- video and extraction of 3 images per second.
- hand labbeling of a few samples then proposals to accelerate with roboflow annotate

# Steps to run the API (uvicorn, etc.)
-launch a server : uvicorn main:app --reload --port 8000  --log-level debug
-check health with : curl http://127.0.0.1:8000/healthcheck/


# Example API call
- call with an image : \
curl 'http://127.0.0.1:8000/predict/' -F 'file=@/home/pierre/experiment_k/app/test_image.jpg'
- image caught on demand : \
curl -F "use_camera=true" http://127.0.0.1:8000/predict/



# Options :
- one (unique) unit test to demonstrate
- retrain with "python retrain.py"





TO DO :
- robustify
- systematic unit tests
- cleaner code
- docker
- logs requests and responses


prioritize:
write read me
docker
logging calls
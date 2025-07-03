# experiment_k
personnal camera tests


python camera.py

first : train
python model.py


python predict.py

uvicorn main:app --reload --port 8000  --log-level debug

curl http://127.0.0.1:8000/healthcheck/

curl 'http://127.0.0.1:8000/predict/'   -F 'file=@/home/pbedu/experiment_k/data/train/images/image-0001_png.rf.48960681266b71a9f81c8dfcb2a3e1bc.jpg'


TO DO :
- robustify
- systematic unit tests
- clean code
- docker
- logs requests and responses


prioritize:
api with camera call

write read me
retrain
docker
logging calls
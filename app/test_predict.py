#unit test for the main function

from predict import predict_fct

def test_predict_fct_detects_two_objects():
    image_path = "/home/pbedu/experiment_k/app/test_image.jpg"
    
    result = predict_fct(image_path)
    
    boxes = result[0].boxes
    predicted_classes = [int(box.cls[0].item()) for box in boxes]
    
    
    assert len(boxes) == 2
    assert set(predicted_classes) == {0, 2}

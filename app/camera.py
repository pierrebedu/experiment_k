# Simulated camera module

import cv2
import os

def capture_image(use_camera=True, image_path=None):

    if use_camera:
        cap = cv2.VideoCapture("/dev/video2")
        if not cap.isOpened():
            raise RuntimeError("Erreur: Caméra non détectée")
        
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            raise RuntimeError("Échec de la capture")
        return frame
        
    else:
        if not image_path or not os.path.exists(image_path):
            raise FileNotFoundError("Fichier image introuvable")
        return cv2.imread(image_path)

if __name__ == "__main__":
    real_image = capture_image(use_camera=True)
    cv2.imwrite("real_image.jpg", real_image)
    
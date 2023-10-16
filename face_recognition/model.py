import os

import cv2
import numpy as np
from PIL import Image

recognizer: cv2.face.LBPHFaceRecognizer
faces_cascade_classifier: cv2.CascadeClassifier
MODEL_PATH = f"face_recognition/model.yml"
CASCADE_CLASSIFIER_PATH = "face_recognition/haarcascade_frontalface_default.xml"


def get_faces() -> tuple[list, np.ndarray]:
    """Used for testing purposes."""

    def is_image(filename: str) -> bool:
        return any(filename.endswith(extension) for extension in ('png', 'jpg', 'jpeg'))

    demo_images_path = "demo_images"

    images = [os.path.join(demo_images_path, f) for f in os.listdir(demo_images_path) if is_image(f)]

    faces = []
    ids = np.array(range(len(images)))

    for img in images:
        face_image = Image.open(img).convert("L")
        face = np.array(face_image)
        faces.append(face)

    return faces, ids


def init_face_recognition_model() -> None:
    global recognizer
    global faces_cascade_classifier

    faces_cascade_classifier = cv2.CascadeClassifier(CASCADE_CLASSIFIER_PATH)
    recognizer = cv2.face.LBPHFaceRecognizer.create()

    faces, ids = get_faces()
    recognizer.train(faces, ids)

    recognizer.save(MODEL_PATH)


def predict(frame: np.ndarray) -> float:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    max_confidence = 0

    for x, y, w, h in faces:
        roi_gray = gray[y : y + h, x : x + w]
        _, confidence = recognizer.predict(roi_gray)
        confidence = 100 - confidence
        if confidence > max_confidence:
            max_confidence = confidence

    return max_confidence / 100

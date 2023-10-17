import os

import cv2
import numpy as np
from PIL import Image

from utils import flatten

recognizer: cv2.face.LBPHFaceRecognizer
faces_cascade_classifier: cv2.CascadeClassifier
MODEL_PATH = f"face_recognition/model.yml"
CASCADE_CLASSIFIER_PATH = "face_recognition/haarcascade_frontalface_default.xml"


def get_faces_from_frame(frame: np.ndarray) -> list[np.ndarray]:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faces_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    return [gray[y : y + h, x : x + w] for x, y, w, h in faces]


def load_demo_images() -> tuple[list, np.ndarray]:
    """Used for testing purposes."""

    def is_image(filename: str) -> bool:
        return any(filename.endswith(extension) for extension in ('png', 'jpg', 'jpeg'))

    def path_to_img(path: str) -> np.ndarray:
        face_image = Image.open(path).convert('RGB')
        face = np.array(face_image)
        return face

    demo_images_path = "demo_images"

    images = [path_to_img(os.path.join(demo_images_path, f)) for f in os.listdir(demo_images_path) if is_image(f)]

    faces = flatten(get_faces_from_frame(image) for image in images)
    ids = np.array([0] * len(faces))

    return faces, ids


def init_face_recognition_model() -> None:
    global recognizer
    global faces_cascade_classifier

    faces_cascade_classifier = cv2.CascadeClassifier(CASCADE_CLASSIFIER_PATH)
    recognizer = cv2.face.LBPHFaceRecognizer.create()

    faces, ids = load_demo_images()
    recognizer.train(faces, ids)

    recognizer.save(MODEL_PATH)


def predict(frame: np.ndarray) -> float:
    faces = get_faces_from_frame(frame)

    max_confidence = 0

    for roi_gray in faces:
        _, confidence = recognizer.predict(roi_gray)
        confidence = 100 - confidence
        if confidence > max_confidence:
            max_confidence = confidence

    return max_confidence / 100

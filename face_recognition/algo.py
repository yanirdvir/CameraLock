from typing import Optional

import numpy as np

from face_recognition.model import predict

CONFIDENT_THRESHOLD = 0.70


def recognize(frame: Optional[np.ndarray]) -> bool:
    if frame is None:
        print("No frame")
        return False

    confidence = predict(frame)
    print(f"Confidence: {confidence}")
    return confidence > CONFIDENT_THRESHOLD

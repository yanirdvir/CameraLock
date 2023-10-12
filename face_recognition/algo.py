FACE_DETECTED = False

CONFIDENT_THRESHOLD = 0.0  # TODO determine this value later


def recognize(frame) -> bool:
    return True
    if predict(frame) > CONFIDENT_THRESHOLD:
        return True
    else:
        return False

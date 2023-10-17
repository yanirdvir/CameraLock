from camera import get_current_frame
from face_recognition import recognize


def authenticate_face() -> bool:
    frame = get_current_frame()
    return recognize(frame)


def authenticate_voice() -> bool:
    # TODO: Implement voice authentication
    return True


def authenticate_word() -> bool:
    # TODO: Implement word authentication
    return True


def is_authenticated() -> bool:
    return authenticate_face() and authenticate_voice() and authenticate_word()

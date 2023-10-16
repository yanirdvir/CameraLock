from threading import Thread
from time import sleep

from camera import get_current_frame, stream
from events import on_failure, on_success
from face_recognition import init_face_recognition_model, recognize


def init():
    init_face_recognition_model()


def main():
    init()

    stream_thread = Thread(target=stream)
    stream_thread.start()

    while stream_thread.is_alive():
        frame = get_current_frame()
        succeeded: bool = recognize(frame)
        if succeeded:
            on_success()
        else:
            on_failure()
        sleep(1)


if __name__ == '__main__':
    main()

from threading import Thread
from time import sleep

from authentication import is_authenticated
from camera import stream
from events import on_failure, on_success
from face_recognition import init_face_recognition_model


def init():
    init_face_recognition_model()


def main():
    init()

    stream_thread = Thread(target=stream)
    stream_thread.start()

    while True:
        if is_authenticated():
            on_success()
        else:
            on_failure()
        sleep(1)


if __name__ == '__main__':
    main()

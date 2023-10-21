from threading import Thread
from time import sleep

from authentication import is_authenticated
from camera import stream
from events import on_failure, on_success
from face_recognition import init_face_recognition_model
from program_manager import start_program, stop_program


def init():
    start_program()
    init_face_recognition_model()


def main():
    init()

    try:
        stream_thread = Thread(target=stream)
        stream_thread.start()

        while True:
            if is_authenticated():
                on_success()
            else:
                on_failure()
            sleep(1)
    except KeyboardInterrupt:
        stop_program()
        raise


if __name__ == '__main__':
    main()

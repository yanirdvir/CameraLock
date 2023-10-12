import threading
from time import sleep

from camera import stream, CURRENT_FRAME
from events import on_success, on_failure
from face_recognition import recognize


def main():
    stream_thread = threading.Thread(target=stream)
    stream_thread.start()

    while stream_thread.is_alive():
        frame = CURRENT_FRAME
        succeeded: bool = recognize(frame)
        if succeeded:
            on_success()
        else:
            on_failure()
        sleep(1)


if __name__ == '__main__':
    main()

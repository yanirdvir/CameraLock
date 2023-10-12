import time

import cv2

CURRENT_FRAME = None


def stream(show_frames: bool = False) -> None:
    global CURRENT_FRAME
    capture = cv2.VideoCapture(0)
    while True:
        _, frame = capture.read()
        CURRENT_FRAME = frame
        if show_frames:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        time.sleep(0.5)
    capture.release()
    cv2.destroyAllWindows()


def get_current_frame():
    return CURRENT_FRAME

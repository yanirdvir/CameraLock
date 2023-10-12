import time

import cv2

CURRENT_FRAME = None


def stream() -> None:
    global CURRENT_FRAME
    capture = cv2.VideoCapture(0)
    while True:
        _, frame = capture.read()
        CURRENT_FRAME = frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == ord("q"):
            break
        time.sleep(0.5)
    capture.release()
    cv2.destroyAllWindows()

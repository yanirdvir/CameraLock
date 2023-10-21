from time import sleep
from typing import Optional

import cv2
import numpy as np

from program_manager import is_program_running

CURRENT_FRAME: Optional[np.ndarray] = None


def stream(show_frames: bool = False) -> None:
    global CURRENT_FRAME
    capture = cv2.VideoCapture(0)
    while is_program_running():
        _, frame = capture.read()
        CURRENT_FRAME = frame
        if show_frames:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        sleep(0.5)
    CURRENT_FRAME = None
    capture.release()
    cv2.destroyAllWindows()


def get_current_frame() -> Optional[np.ndarray]:
    return CURRENT_FRAME

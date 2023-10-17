from datetime import datetime
from enum import Enum
from pathlib import Path

from playsound import playsound

SECONDS_BETWEEN_DIFFERENT_EVENTS = 5


class Event(Enum):
    ON_SUCCESS = "on_success"
    ON_FAILURE = "on_failure"
    NO_EVENT = "no_event"


last_event = Event.NO_EVENT
last_event_changed_time = datetime.now()


def play_success_sound() -> None:
    print("Playing success sound...")

    filename = "events/sounds/success_sound.mp3"
    filename = Path(filename)
    playsound(filename)


def update_event_changed(new_event: Event) -> bool:
    global last_event
    global last_event_changed_time

    if (
        last_event != new_event
        and (datetime.now() - last_event_changed_time).total_seconds() >= SECONDS_BETWEEN_DIFFERENT_EVENTS
    ):
        last_event = new_event
        last_event_changed_time = datetime.now()
        return True
    return False


def on_success() -> None:
    print("Success!")
    if not update_event_changed(Event.ON_SUCCESS):
        return

    play_success_sound()


def on_failure() -> None:
    print("Failure!")
    if not update_event_changed(Event.ON_FAILURE):
        return

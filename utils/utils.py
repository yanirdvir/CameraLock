from typing import Iterable


def flatten(_iterable: Iterable) -> list:
    return [item for sublist in _iterable for item in sublist]

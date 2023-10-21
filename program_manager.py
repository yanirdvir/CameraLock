program_running: bool = False


def start_program() -> None:
    global program_running
    program_running = True


def stop_program() -> None:
    global program_running
    program_running = False


def is_program_running() -> bool:
    return program_running

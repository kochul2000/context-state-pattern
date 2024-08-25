from .base.abstract import Context, State


class Initial(State):
    def handle(self) -> None:
        print("hello device")


class Device(Context):
    # Device task
    initial_state_class = Initial

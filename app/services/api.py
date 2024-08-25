from .base.abstract import Context, State


class Initial(State):
    def handle(self) -> None:
        print("hello api")


class Api(Context):
    # communication with server
    initial_state_class = Initial


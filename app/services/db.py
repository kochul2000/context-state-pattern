from .base.abstract import Context, State


class Initial(State):
    def handle(self) -> None:
        print("hello db")


class Db(Context):
    # Database task
    initial_state_class = Initial

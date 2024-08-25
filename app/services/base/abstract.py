import threading
import time
import os
from abc import ABC, abstractmethod


DEBUG = os.getenv("DEBUG", "False").lower() == "true"


class State(ABC):
    """
    Each service's specific states are implemented by inheriting from this State,
    with behaviors defined for each state.
    """
    def __init__(self):
        self._context = None

    @property
    def context(self) -> "Context":
        return self._context

    @context.setter
    def context(self, context: "Context") -> None:
        self._context = context

    @abstractmethod
    def handle(self) -> None | float:
        """
        Defines the behavior for each state.
        Each state has only one handle method.

        return: float - the loop interval in seconds. If not returned, the default interval is applied.
        """
        pass

    # # example code
    # @abstractmethod
    # def handle1(self) -> None:
    #    pass
    #
    # def handle1(self) -> None:
    #     self.context.transition_to(ConcreteStateA())


class Context(ABC):
    """
    Each service is implemented by inheriting from the Context class.
    Follows the State design pattern; see the reference below.
    https://refactoring.guru/ko/design-patterns/state/python/example
    """
    initial_state_class: type[State]
    loop_interval: float = 1

    def __init__(self):
        self._state = None
        self.transition_to(self.initial_state_class())

    def transition_to(self, state: "State") -> None:
        """
        State transition
        """
        self._state = state
        self._state.context = self

    def on_shutdown(self) -> None:
        """
        On service shutdown
        """
        pass

    def loop(self, shutdown_flag: threading.Event) -> None:
        """
        this is the service's main loop and entry point for execution.
        """
        while not shutdown_flag.is_set():
            loop_interval = None
            try:
                loop_interval = self._state.handle()
            except Exception as e:  # noqa
                if DEBUG:
                    print(f"Error: {e}")
                self._state = self.initial_state_class()
            time.sleep(loop_interval or self.loop_interval)

        self.on_shutdown()

    # # example code
    # def request1(self):
    #     self._state.handle1()
    #
    # def request2(self):
    #     self._state.handle2()

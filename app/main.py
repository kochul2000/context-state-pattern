# /opt/app/main.py
# entrypoint of the application
import signal
import threading

from services.base.abstract import Context
from services import Api, Db, Device


class Main:
    def __init__(self, services: list[Context]):
        self.services = services
        self._shutdown_flag = threading.Event()
        self.thread_list = []

        self._setup_signals()
        self._setup_threads()

    def _setup_signals(self):
        """
        shutdown signal setup
        """
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _setup_threads(self):
        """
        for thread handling
        """
        for service in self.services:
            thread = threading.Thread(target=service.loop, args=(self._shutdown_flag,))
            self.thread_list.append(thread)

    def _signal_handler(self, _sig, _frame):
        """
        the second parameter of signal.signal()
        """
        self._shutdown_flag.set()

    def start(self):
        for thread in self.thread_list:
            thread.start()
        print('All services started')

        # The program remains this statement after starting.
        for thread in self.thread_list:
            thread.join()

        self.after_shutdown()

    def after_shutdown(self):
        print('after_shutdown')


if __name__ == '__main__':
    # # # Key Principles # # #
    # * Each component service of the program applies the State design pattern.
    # * Each running service operates in its own separate thread.
    # * Each running service inherits from a context to form its own context.
    # * The connections between services are managed in this file's Context using Queues and similar mechanisms.
    print("start main")

    services = [
        Db(),
        Api(),
        Device()
    ]
    main = Main(services)
    main.start()

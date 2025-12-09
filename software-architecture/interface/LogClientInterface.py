from abc import ABC, abstractmethod

class LogClientInterface(ABC):
    @abstractmethod
    def send_log(self, log: str):
        pass
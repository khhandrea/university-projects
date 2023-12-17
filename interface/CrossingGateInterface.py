from abc import ABC, abstractmethod

class CrossingGateInterface(ABC):
    @abstractmethod
    def set_opened(self):
        pass
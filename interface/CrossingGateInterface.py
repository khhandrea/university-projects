from abc import ABC, abstractmethod

class CrossingGateInterface(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

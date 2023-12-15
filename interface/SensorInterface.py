from abc import ABC, abstractmethod

class SensorInterface(ABC):
    @abstractmethod
    def capture(self):
        pass
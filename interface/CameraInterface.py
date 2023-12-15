from abc import ABC, abstractmethod

class CameraInterface(ABC):
    @abstractmethod
    def capture(self):
        pass
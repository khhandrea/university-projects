from abc import ABC, abstractmethod

class LoopCoilSensorInterface(ABC):
    @abstractmethod
    def set_detected(self, detected : bool):
        pass

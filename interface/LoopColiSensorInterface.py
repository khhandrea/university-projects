from abc import ABC, abstractmethod

class LoopCoilSensorInterface(ABC):
    @abstractmethod
    def signal(self, car_pass: bool):
        pass

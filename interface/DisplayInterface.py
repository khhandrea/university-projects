from abc import ABC, abstractmethod

class DisplayInterface(ABC):
    @abstractmethod
    def print(self, car_info: dict, fee: int):
        pass

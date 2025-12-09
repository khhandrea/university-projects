from abc import ABC, abstractmethod

class DisplayInterface(ABC):
    @abstractmethod
    def display_print(self, car_info: dict, fee: int):
        pass

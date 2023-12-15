from abc import ABC, abstractmethod

class PayModuleInterface(ABC):
    @abstractmethod
    def pay(self, cost: int, method):
        pass
    
    @abstractmethod
    def process_pay(self, cost: int, method):
        pass
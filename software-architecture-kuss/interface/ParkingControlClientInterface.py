from abc import ABC, abstractmethod

class ParkingCntrolClientInterface(ABC):
    @abstractmethod
    def get_discount_info(self):
        pass
    
    @abstractmethod
    def insert_current_car(self, car_num: str):
        pass

    @abstractmethod
    def delete_current_car(self, car_num: str):
        pass

    @abstractmethod
    def get_broker_url(self, location: str):
        pass
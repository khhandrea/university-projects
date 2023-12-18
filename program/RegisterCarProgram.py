from json import dumps, loads
import sys
from typing import Tuple
from time import sleep
from os.path import dirname, abspath
from queue import Queue

sys.path.append(dirname(abspath(dirname(__file__))))
import MQTTclient
from program import Program, DBRepository

queue_from_user = Queue()
queue_from_pay_module = Queue()

class RegisterCarProgram(Program):
    def __init__(self, config, topic_dispatcher):
        self.config = config
        self.topic_dispatcher = topic_dispatcher
        self.register_car_server = RegisterCarServer(config=config)
        self.register_fee = 90000

        config_output = {
            "ip": "127.0.0.1", 
            "port": 60507, 
            "topics": [
                ("hardware/server/registerCarProgram/to", 0),
                ("hardware/server/parkingDB/from", 0),
                ("hardware/server/schoolDB/from", 0)
            ],
        }

        self.publisher_output = MQTTclient.Publisher(config=config_output)
        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        while True:
            if not queue_from_user.empty():
                car_number, car_type, identification = queue_from_user.get()
                message = self.register_car(car_number, car_type, identification)
                print('message:', message)
                self.publisher_output.publish("hardware/server/registerCarProgram/from", message)

    def register_car(self, car_number: str, car_type: str, identification: int):

        certificated = self.register_car_server.request_member_info(identification)
        if not self.check_valid_info(certificated, identification):
            return 'Invalid user'
        
        car_info = self.register_car_server.request_car_type(car_type)
        if not self.check_valid_car_type(car_info):
            return 'Invalid car type'
            
        fee = self.calculate_cost(car_info)
        if fee == 0:
            self.register_car_server.register_car(identification, car_number)
        else:
            self.pay(fee)
            self.register_car_server.register_car(identification, car_number)
        return 'Registered successfully'

    def check_valid_info(self, certificated: Tuple, identification: int) -> bool:
        if certificated == None:
            return False
        else:
            if certificated[0] == identification:
                return True
            else:
                False

    def check_valid_car_type(self, car_info: Tuple) -> bool:
        if car_info == None:
            return False
        else:
            return True

    def calculate_cost(self, car_info: Tuple) -> int:
        _, sale_amount = car_info
        result = int(self.register_fee * (1 - int(sale_amount) / 100))
        return result

    def pay(self, cost):
        message = f"결제모듈_차량등록서버/{cost}"
        print('send message to paymodule', message)
        self.publisher.publish('hardware/server/paymodule/to', message)

        while queue_from_pay_module.empty():
            pass

        data = queue_from_pay_module.get()

        print(data)
        



class RegisterCarServer(Program):
    def __init__(self, config):
        self.config = config
        self.pos = '차량등록서버'
        self.school_db_publisher = DBRepository(self.pos, 'schoolDB')
        self.parking_db_publisher = DBRepository(self.pos, 'parkingDB')

    def request_member_info(self, identification) -> Tuple:
        data = {
            'type': 'get',
            'target': 'school_member',
            'pos': self.pos,
            'pk': {
                'id': identification
            }
        }
        data = dumps(data)
        
        data = self.school_db_publisher.get(data)
        print('got', data, 'from school')
        if data == 'None':
            None
        else:
            data = data[1:-1].split(', ')
        return data


    def request_car_type(self, car_type) -> Tuple:
        data = {
            'type': 'get',
            'target': 'sale',
            'pos': self.pos,
            'pk': {
                'car_type': car_type
            }
        }
        data = dumps(data)
        data = self.parking_db_publisher.get(data)
        print('got', data, 'from ')
        if data == 'None':
            None
        else:
            data = data[1:-1].split(', ')
        return data

    def register_car(self, identification: int, car_number: str) -> str:
        data = {
            'type': 'insert',
            'target': 'register',
            'pos': self.pos,
            'item': {
                'id': identification,
                'car_number': car_number
            }
        }
        data = dumps(data)
        self.parking_db_publisher.insert(data)

def handle_register(topic, data, publisher):
    print(f'{data} to register')
    data = data.split("/")
    queue_from_user.put(data)

def handle_pay_module(topic, data, publisher):
    print(f'{data} to register')
    data = data.split("/")
    queue_from_pay_module.put(data)

if __name__ == '__main__':

    config = {
            "ip": "127.0.0.1", 
            "port": 60406, 
            "topics": [
                ("hardware/server/registerCarProgram/to", 0),
                ("hardware/server/paymodule/from", 0)
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/registerCarProgram/to": handle_register,
        "hardware/server/paymodule/from": handle_pay_module
    }

    register_car_program = RegisterCarProgram(config=config, topic_dispatcher=topic_dispatcher)
    register_car_program.start()
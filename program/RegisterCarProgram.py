from json import dumps, loads
import sys
from typing import Tuple
from time import sleep
from os.path import dirname, abspath
from queue import Queue

sys.path.append(dirname(abspath(dirname(__file__))))
import MQTTclient
from program import Program

queue_from_user = Queue()
queue_from_school_db = Queue()
queue_from_parking_db = Queue()

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

    def check_valid_info(self, certificated: Tuple, identification: Tuple) -> bool:
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
        result = int(self.register_fee * (int(sale_amount) / 100))
        return result

    def pay(cost):
        print('pay')

class RegisterCarServer(Program):
    def __init__(self, config):
        self.config = config
        self.publisher = MQTTclient.Publisher(config=self.config)

    def request_member_info(self, identification) -> Tuple:
        data = {
            'type': 'get',
            'target': 'school_member',
            'pk': {
                'id': identification
            }
        }
        data = dumps(data)
        self.publisher.publish("hardware/server/schoolDB/to", data)

        while queue_from_school_db.empty():
            pass

        data = queue_from_school_db.get()
        return data


    def request_car_type(self, car_type) -> Tuple:
        data = {
            'type': 'get',
            'target': 'sale',
            'pk': {
                'car_type': car_type
            }
        }
        data = dumps(data)
        self.publisher.publish("hardware/server/parkingDB/to", data)

        while queue_from_parking_db.empty():
            pass

        return queue_from_parking_db.get()

    def register_car(self, identification: int, car_number: str) -> str:
        data = {
            'type': 'insert',
            'target': 'register',
            'item': {
                'id': identification,
                'car': car_number
            }
        }
        data = dumps(data)
        self.publisher.publish("hardware/server/parkingDB/to", data)

def handle_register(topic, data, publisher):
    print(f'got {data} to register')
    data = data.split("/")
    queue_from_user.put(data)

def handle_schoolDB(topic, data, publisher):
    print(f'got {data} from school')
    if data == 'None':
        data = None
    else:
        data = data[1:-1].split(', ')
    queue_from_school_db.put(data)

def handle_parkingDB(topic, data, publisher):
    print(f'got {data} from parking')
    if data == 'None':
        data = None
    else:
        data = data[1:-1].split(', ')
    queue_from_parking_db.put(data)

if __name__ == '__main__':

    config = {
            "ip": "127.0.0.1", 
            "port": 60406, 
            "topics": [
                ("hardware/server/registerCarProgram/to", 0),
                ("hardware/server/parkingDB/from", 0),
                ("hardware/server/schoolDB/from", 0)
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/registerCarProgram/to": handle_register,
        "hardware/server/schoolDB/from": handle_schoolDB,
        "hardware/server/parkingDB/from": handle_parkingDB,
    }

    register_car_program = RegisterCarProgram(config=config, topic_dispatcher=topic_dispatcher)
    register_car_program.start()
import sys
from os.path import dirname, abspath
from json import loads
from queue import Queue

sys.path.append(dirname(abspath(dirname(__file__))))
from program import Program
from program.DBHandler import DBHandler

queue = Queue()

class ParkingDBHandler(Program, DBHandler):
    def __init__(self, config, topic_dispatcher):
        self.config = config
        self.topic_dispatcher = topic_dispatcher
        
        location = 'database/parking.db'

        Program.__init__(self, self.config, self.topic_dispatcher)
        DBHandler.__init__(self, location)  

    def start(self):
        while True:
            if not queue.empty():
                data = queue.get()
                message = self.handle(data).encode('euc-kr')
                print(f'send {message} to "hardware/server/parkingDB/from"')
                self.publisher.publish("hardware/server/parkingDB/from", message)

def handle_parkingDB(topic, data, publisher):
    print(f'got message {data} from {topic}')
    data = loads(data)
    queue.put(data)

if __name__ == '__main__':

    config = {
            "ip": "127.0.0.1", 
            "port": 1883, 
            "topics": [
                ("hardware/server/parkingDB/to", 0),
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/parkingDB/to": handle_parkingDB,
    }

    parking_db_handler = ParkingDBHandler(config=config, topic_dispatcher=topic_dispatcher)
    parking_db_handler.start()
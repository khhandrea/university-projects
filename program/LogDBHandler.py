from datetime import datetime
import sys
from os.path import dirname, abspath
from json import loads
from queue import Queue

sys.path.append(dirname(abspath(dirname(__file__))))
from program import Program
from program.DBHandler import DBHandler

queue = Queue()

class LogDBHandler(Program, DBHandler):
    def __init__(self, config, topic_dispatcher):
        self.config = config
        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

        Program.__init__(self, self.config, self.topic_dispatcher)
        DBHandler.__init__(self, None)

    def start(self):
        while True:
            if not queue.empty():
                data = queue.get()
                
                assert data['type'].lower() == 'insert'
                assert data['target'].lower() == 'log'

                self.handle(data)

    # override
    def _insert(self, target: str, item: dict):
        with open('../database/log.db', 'a') as file:
            message = item['message']
            time = datetime.now().strftime('%Y%m%d_%H%M%S')
            log = f"({time}){message}\n"
            print(log, end='')
            file.write(log)
        

def handle_log(topic, data, publisher):
    print(f'got {data}')
    data = loads(data)
    queue.put(data)

if __name__ == '__main__':
    config = {
            "ip": "127.0.0.1", 
            "port": 60906, 
            "topics": [
                ("hardware/server/logDB/to", 0)
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/logDB/to": handle_log,
    }

    db_handler = LogDBHandler(config=config, topic_dispatcher=topic_dispatcher)
    db_handler.start()
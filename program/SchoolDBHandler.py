import sys
from os.path import dirname, abspath
from json import loads
from queue import Queue

sys.path.append(dirname(abspath(dirname(__file__))))
from program import Program
from program.DBHandler import DBHandler

queue = Queue()

class SchoolDBHandler(Program, DBHandler):
    def __init__(self, config, topic_dispatcher):
        self.config = config
        self.topic_dispatcher = topic_dispatcher
        
        location = '../database/school.db'

        Program.__init__(self, self.config, self.topic_dispatcher)
        DBHandler.__init__(self, location)  

    def start(self):
        while True:
            if not queue.empty():
                data = queue.get()
                pos = data['pos']
                message = self.handle(data).encode('euc-kr')
                topic = f"hardware/server/schoolDB/{pos}/from"
                print(f'send {message} to topic')
                self.publisher.publish(topic, message)

def handle_schoolDB(topic, data, publisher):
    print(f'got message {data} from {topic}')
    data = loads(data)
    queue.put(data)

if __name__ == '__main__':

    config = {
            "ip": "127.0.0.1", 
            "port": 60906, 
            "topics": [
                ("hardware/server/schoolDB/to", 0),
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/schoolDB/to": handle_schoolDB,
    }

    school_db_handler = SchoolDBHandler(config=config, topic_dispatcher=topic_dispatcher)
    school_db_handler.start()
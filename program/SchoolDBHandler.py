import sys
from os import dirname, abspath
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
        
        location = 'database/school.db'

        Program.__init__(self, self.config, self.topic_dispatcher)
        DBHandler.__init__(self, location)  

    def start(self):
        while True:
            if not queue.empty():
                data = queue.get()
                message = self.handle(data)
                self.publisher.publish("hardware/server/schoolDB/from", message)

def handle_schoolDB(topic, data, publisher):
    data = loads(data.decode('utf-8'))
    queue.put(data)

if __name__ == '__main__':

    config = {
            "ip": "127.0.0.1", 
            "port": 1883, 
            "topics": [
                ("hardware/server/schoolDB/to", 0),
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/schoolDB/to": handle_schoolDB,
    }

    school_db_handler = SchoolDBHandler(config=config, topic_dispatcher=topic_dispatcher)
    school_db_handler.start()
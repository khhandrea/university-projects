import sys, os, json, argparse
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
import time

from hardware.CrossingGate import CrossingGate

"""

고쳐야할 것:
  - ProgramExample - start
  - config
  - topic_dispathcer


def callback_example(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")

--> 이런 식으로 (topic, data, publisher)를 무조건 받아야함.

"""

class DBRepository(Program):
    def __init__(self, config):
        self.config = config


        self.topic_dispatcher = {
            "hardware/server/parkingDB/to": self.handle_in,
        }

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        pass

    def get(self, qeury):
        pass

    def insert(self, query):
        pass

    def update(self, query):
        pass

    def delete(self, query):
        pass


        

if __name__ == '__main__':
    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 60906, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                ("hardware/server/parkingDB/from", 0), 
            ],
        }

    ex = DBRepository(config=config)
    ex.start()
    


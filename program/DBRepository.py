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
    def __init__(self, pos, db_name):
        self.pos = pos
        self.topic_to = f"hardware/server/{db_name}/to"
        self.topic_from = f"hardware/server/{db_name}/{self.pos}/from"


        self.config = {
            "ip": "127.0.0.1", 
            "port": 60906, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (self.topic_from, 0), 
            ],
        }
        self.queue_msg = Queue()

        self.topic_dispatcher = {
            self.topic_from: self.handle_get,
        }

        super().__init__(self.config, self.topic_dispatcher)

    def get(self, query):
        self.publisher.publish(self.topic_to, query)
        
        # queue.get() wait for data
        data = self.queue_msg.get(timeout=3)

        if data:
            return data

    def insert(self, query):
        self.publisher.publish(self.topic_to, query)
        
        # queue.get() wait for data
        data = self.queue_msg.get()

        if data:
            return data

    def update(self, query):
        self.publisher.publish(self.topic_to, query)
        
        # queue.get() wait for data
        data = self.queue_msg.get()

        if data:
            return data

    def delete(self, query):
        self.publisher.publish(self.topic_to, query)
        
        # queue.get() wait for data
        data = self.queue_msg.get()

        if data:
            return data

    def handle_get(self, topic, data, publisher):
        self.queue_msg.put(data)
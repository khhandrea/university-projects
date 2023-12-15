import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
import time


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

class ProgramExample(Program):
    def __init__(self, config, topic_dispatcher):
        self.config = config
        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            self.publisher.publish("hardware/sensors/loopcoil", "ji")
            time.sleep(1)

    
# TODO 각자에 맞게 추가하면 됨
def handle_loopcoil(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")
    publisher.publish("hihihi", "hihi")

def handle_crossinggate(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")

if __name__ == '__main__':


    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 1883, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                ("hardware/sensors/loopcoil", 0), 
                ("hardware/crossinggate", 0)
            ],
        }
    
    # TODO 각자에 맞게 고치면 됨
    # topic: handler 순으로 추가하면 된다.
    # 원하는 topic에 해당하는 반응을 구현하면 됨
    topic_dispatcher = {
        "hardware/sensors/loopcoil": handle_loopcoil,
        "hardware/crossinggate": handle_crossinggate,
    }

    ex = ProgramExample(config=config, topic_dispatcher=topic_dispatcher)
    ex.start()
    


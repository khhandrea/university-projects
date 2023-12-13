import MQTTclient

from queue import Queue
from multiprocessing import Process
from program import Program


"""

고쳐야할 것:
  - topic_dispathcer
  - handler


def callback_example(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")

--> 이런 식으로 (topic, data, publisher)를 무조건 받아야함.

"""

def handle_loopcoil(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")

def handle_crossinggate(topic, data, publisher):
    print(f"topic: {topic}")
    print(f"data: {data}")

if __name__ == '__main__':

    config = {
        "ip": "127.0.0.1", 
        "port": 6007, 
        "topics": ["hardware/sensors/loopcoil", "hardware/crossinggate"],
        }
    
    topic_dispatcher = {
        "hardware/sensors/loopcoil": handle_loopcoil,
        "hardware/crossinggate": handle_crossinggate,
    }

    example_program = Program

    

    queue = Queue()

    program = Program(config=config)



    
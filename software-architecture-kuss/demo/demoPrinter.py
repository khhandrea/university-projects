import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from queue import Queue
from program import Program



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


class demoPrinter(Program):
    def __init__(self, config):
        self.config = config

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            "demo/print": self.handle_print,
        }
        self.topic_dispatcher = topic_dispatcher
        self.queue_msg = Queue()

        super().__init__(self.config, self.topic_dispatcher)

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            print(self.queue_msg.get())

    def handle_print(self, topic, data, publisher):
        self.queue_msg.put(data)

if __name__ == '__main__':

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 60507, 
            "topics": [("demo/print", 0)],
        }

    demo_program = demoPrinter(config=config)
    demo_program.start()
    

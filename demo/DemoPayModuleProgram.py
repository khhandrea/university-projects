import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient
from program import Program
from hardware import PayModule



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


class PayModuleProgram(Program):
    def __init__(self, pay_module: PayModule):
        self.pay_module = pay_module

        self.pos = self.pay_module.get_pos()
        self.name = "결제모듈_" + self.pos
        self.door, self.direction = self.pos.split("_")

        self.demo_publisher = MQTTclient.DemoPublisher()

        self.direction = "in" if self.direction == "입차방향" else "out"
        self.config = {
            "ip": "127.0.0.1", 
            "port": 60506, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (f"demo/hardware/pay_module/{self.direction}/to/broken", 0), 
            ],
        }

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            f"demo/hardware/pay_module/{self.direction}/to/broken": self.handle_broken,
        }

        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

    
    def handle_broken(self, topic, data, publisher):
        assert data in ['고장', '정상'], f'Data should be "True" or "False". Topic from "{topic}"'
        
        if data == '고장':
            self.demo_publisher.demo_print(f"[{self.name}] 현재 상태 : {self.pay_module.get_status()}")
            self.pay_module.set_status('고장')
            self.demo_publisher.demo_print(f"[{self.name}] {self.pay_module.get_status()}으로 변경되었습니다.")
        elif data == '정상':
            self.demo_publisher.demo_print(f"[{self.name}] 현재 상태 : {self.pay_module.get_status()}")
            self.pay_module.set_status('정상')
            self.demo_publisher.demo_print(f"[{self.name}] {self.pay_module.get_status()}으로 변경되었습니다.")
    


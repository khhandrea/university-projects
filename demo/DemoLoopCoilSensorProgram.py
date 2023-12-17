import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient
from program import Program
from hardware import LoopCoilSensor



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


class DemoLoopCoilSensorProgram(Program):
    def __init__(self, loop_coil_sensor: LoopCoilSensor):

        self.loop_coil_sensor = loop_coil_sensor

        self.pos = self.loop_coil_sensor.get_pos()
        self.name = "바닥센서_" + self.pos
        self.door, self.direction, self.num = self.pos.split("_")

        self.demo_publisher = MQTTclient.DemoPublisher()

        self.direction = "in" if self.direction == "입차방향" else "out"
        
        if '상허문' in self.pos:
            port = 60606
        elif '일감문' in self.pos:
            port = 60706
        elif '건국문' in self.pos:
            port = 60806
        else:
            raise ValueError("Wrong position")

        self.config = {
            "ip": "127.0.0.1", 
            "port": port, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (f"demo/hardware/loop_coil_sensor/{self.direction}/{self.num}/to/broken", 0), 
                (f"demo/hardware/loop_coil_sensor/{self.direction}/{self.num}/to/recognition", 0), 
            ],
            
        }

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            f"demo/hardware/loop_coil_sensor/{self.direction}/{self.num}/to/broken": self.handle_broken,
            f"demo/hardware/loop_coil_sensor/{self.direction}/{self.num}/to/recognition": self.handle_recognition
        }

        self.topic_dispatcher = topic_dispatcher

        

        super().__init__(self.config, self.topic_dispatcher)

    
    def handle_broken(self, topic, data, publisher):
        assert data in ['고장', '정상'], f'Data should be "고장" or "정상". Topic from "{topic}"'

        if data == '고장':
            self.demo_publisher.demo_print(f"[{self.name}] 현재 상태 : {self.loop_coil_sensor.get_status()}")
            self.loop_coil_sensor.set_status('고장')
            self.demo_publisher.demo_print(f"[{self.name}] {self.loop_coil_sensor.get_status()}으로 변경되었습니다.")
        elif data == '정상':
            self.demo_publisher.demo_print(f"[{self.name}] 현재 상태 : {self.loop_coil_sensor.get_status()}")
            self.loop_coil_sensor.set_status('정상')
            self.demo_publisher.demo_print(f"[{self.name}] {self.loop_coil_sensor.get_status()}으로 변경되었습니다.")
    
    def handle_recognition(self, topic, data, publisher):
        assert data in ['True', 'False'], f'Data should be "True" or "False". Topic from "{topic}"'

        if data == 'True':
            self.demo_publisher.demo_print(f"[{self.name}] 코일이 감지되었습니다.")
            self.loop_coil_sensor.set_detected(True)
        elif data == 'False':
            self.demo_publisher.demo_print(f"[{self.name}] 코일 감지가 해제되었습니다.")
            self.loop_coil_sensor.set_detected(False)


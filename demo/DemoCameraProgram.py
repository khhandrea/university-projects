import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from program import Program
from hardware import Camera



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


class CameraProgram(Program):
    def __init__(self, camera: Camera):
        self.camera = camera

        self.pos = self.camera.get_pos()
        self.door, self.direction = self.pos.split("_")

        self.direction = "in" if self.direction == "입차방향" else "out"

        self.config = {
            "ip": "127.0.0.1", 
            "port": 60506, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (f"demo/hardware/camera/{self.direction}/to/broken", 0), 
            ],
        }

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            f"demo/hardware/camera/{self.direction}/to/broken": self.handle_broken,
        }

        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

    
    def handle_broken(self, topic, data, publisher):
        if data == '고장':
            self.camera.set_status('고장')
        elif data == '정상':
            self.camera.set_status('정상')
    


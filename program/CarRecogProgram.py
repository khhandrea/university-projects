import sys, os, json
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
from datetime import datetime

import argparse

from hardware.Camera import Camera

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

class CarRecogProgram(Program):
    def __init__(self, config, pos):
        self.config = config
        if "입차" in self.pos:
            # 입차의 경우 in topic을 subscribe
            self.topic_dispatcher = {
                "hardware/server/car_recog/in/to": self.handle_capture_in,
                "monitoring": self.handle_monitoring
            }
        elif "출차" in self.pos:
            # 출차의 경우 out topic을 subscribe
            self.topic_dispatcher = {
                "hardware/server/car_recog/out/to": self.handle_capture_out,
                "monitoring": self.handle_monitoring
            }

        self.camera = Camera(pos)

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        pass


    def handle_capture_in(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        img = self.camera.capture()
        car_num = self.img_to_carnum(img)
        now = datetime.now()
        publisher.publish('hardware/server/car_recog/in/from', f'{now.strftime("%Y%m%d_%H%M%S")}/{car_num}')

    def handle_capture_out(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        img = self.camera.capture()
        car_num = self.img_to_carnum(img)
        now = datetime.now()
        publisher.publish('hardware/server/car_recog/out/from', f'{now.strftime("%Y%m%d_%H%M%S")}/{car_num}')

    def handle_monitoring(self, topic, data, publisher):
        state = {
            "cpu" : 0.7,
            "ram" : 0.5,
            "temperature" : 30,
            "state" : None,
            "available" : self.camera.get_status()
        }
        state_message = json.dumps(state)
        self.publisher.publish("monitoring/camera", state_message)

    def img_to_carnum(self, img):
        return img[0]

        

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-pos', '--position', type=str, default="")
    args = argparser.parse_args()

    pos = args.position
    if pos == '상허문_입차방향' or pos == '상허문_출차방향':
        port = 60606
    elif pos == '일감문_입차방향' or pos == '일감문_출차방향':
        port = 60706
    elif pos == '건국문_입차방향' or pos == '건국문_출차방향':
        port = 60806
    else:
        raise ValueError("Wrong position")

    config = {
            "ip": "127.0.0.1", 
            "port": port,
            "topics": [
                ("hardware/server/crossing_gate/in/to", 0), 
                ("hardware/server/crossing_gate/out/to", 0)
            ],
        }
    
    # TODO argparser로 방향 입력
    ex = CarRecogProgram(config=config, pos=pos)
    ex.start()
    


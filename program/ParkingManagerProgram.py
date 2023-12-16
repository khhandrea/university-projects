import sys, os, json
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
from datetime import datetime

import argparse

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

class ParkingManagerProgram(Program):
    def __init__(self, config, pos):
        self.config = config
        self.pos = pos
        self.topic_dispatcher = {
            'hardware/server/loop_coil/in/1/from': self.handle_loop_coil_in_1,
            'hardware/server/loop_coil/in/2/from': self.handle_loop_coil_in_2,
            'hardware/server/loop_coil/out/1/from': self.handle_loop_coil_out_1,
            'hardware/server/loop_coil/out/2/from': self.handle_loop_coil_out_2,
            'hardware/server/car_recog/in/from': self.handle_car_recog_in,
            'hardware/server/car_recog/out/from': self.handle_car_recog_out,
            'hardware/server/paymodule/from': self.handle_paymodule
        }

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        pass


    def handle_loop_coil_in_1(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        publisher.publish('hardware/server/car_recog/in/to', 'capture')
        publisher.publish('hardware/server/crossing_gate/in/to', 'open')
    
    def handle_loop_coil_in_2(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        publisher.publish('hardware/server/crossing_gate/in/to', 'close')


    def handle_loop_coil_out_1(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        publisher.publish('hardware/server/car_recog/out/to', 'capture')

    def handle_loop_coil_out_2(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        publisher.publish('hardware/server/crossing_gate/out/to', 'close')

    def handle_car_recog_in(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        # DB에 로그 저장

    def handle_car_recog_out(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        self.out_time, self.car_num = data.split('/')
        # 로그 불러오기 (입차 시간)

        # 요금 계산 (할인율 확인)

        # display에 출력

        # 장애인 차량 여부 확인 (입력)

        # 결제 수단 요청 (입력)
        
        # 결제 모듈 (요청)

        # DB에 로그 저장
    
    def handle_paymodule(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        # 성공했을 시, 문 열기
        if "True" in data:
            publisher.publish('hardware/server/crossing_gate/out/to', 'open')
            self.out_time, self.car_num = "", ""
        else:
            publisher.publish('hardware/server/car_recog/out/from', self.out_time+"/"+self.car_num)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-pos', '--position', type=str, default="")
    args = argparser.parse_args()

    pos = args.position
    if pos == '상허문':
        port = 60606
    elif pos == '일감문':
        port = 60706
    elif pos == '건국문':
        port = 60806
    else:
        raise ValueError("Wrong position")

    config = {
            "ip": "127.0.0.1", 
            "port": port,
            "topics": [
                ('hardware/server/loop_coil/in/1/from', 0),
                ('hardware/server/loop_coil/in/2/from', 0),
                ('hardware/server/loop_coil/out/1/from', 0),
                ('hardware/server/loop_coil/out/2/from', 0),
                ('hardware/server/car_recog/in/from', 0),
                ('hardware/server/car_recog/out/from', 0),
                ('hardware/server/paymodule/from', 0)
            ],
        }
    
    ex = ParkingManagerProgram(config=config, pos=pos)
    ex.start()
    


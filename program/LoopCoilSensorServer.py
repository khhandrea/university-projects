import sys, os, json, argparse
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
import time
from datetime import datetime
from hardware.LoopCoilSensor import LoopCoilSensor

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

class LoopCoilSensorServer(Program):
    def __init__(self, config, pos):
        self.config = config
        self.pos = pos
        self.topic_dispatcher = {
            "monitoring": self.handle_monitoring
        }
        self.loop_coil_sensor_1 = LoopCoilSensor(pos+'_1')
        self.loop_coil_sensor_2 = LoopCoilSensor(pos+'_2')
        self.log_publisher = MQTTclient.LogPublisher()
        self.demo_publisher = MQTTclient.DemoPublisher()

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        if self.pos[-4:] == '입차방향':
            pos = 'in'
        else:
            pos = 'out'
        cur_status = 0

        while True:
            coil_1_detected = self.loop_coil_sensor_1.get_detected()
            if cur_status == 0 and coil_1_detected:
                now = datetime.now()
                self.publisher.publish(f'hardware/server/loop_coil/{pos}/1/from', f'{now.strftime("%Y%m%d_%H%M%S")}/True') # 게이트로 들어옴 신호
                cur_status = 1
                log = f"[바닥센서_{self.pos}_1] (인식: True)"
                self.log_publisher.log(log)
                self.demo_publisher.demo_print(log)
    
            coil_2_detected = self.loop_coil_sensor_2.get_detected()
            # 차량이 통과할 때까지 확인 / 대기
            if cur_status == 1 and coil_2_detected:
                now = datetime.now()
                self.publisher.publish(f'hardware/server/loop_coil/{pos}/2/from', f'{now.strftime("%Y%m%d_%H%M%S")}/True') # 게이트에서 나감 신호
                print(f"topic: hardware/server/loop_coil/{pos}/2/from")
                print(f'data: {now.strftime("%Y%m%d_%H%M%S")}/True')
                cur_status = 0
                log = f"[바닥센서_{self.pos}_2] (인식: True)"
                self.log_publisher.log(log)
                self.demo_publisher.demo_print(log)

            time.sleep(0.5)

    # topics에 ("monitoring", 0) 추가
    # topic_dispatcherd에 "monitoring" : self.handle_monitoring 추가
    def handle_monitoring(self, topic, data, publisher):
        state = {
            "pos" : "바닥센서_" + self.pos + "_1",
            "cpu" : 0.7,
            "ram" : 0.5,
            "temperature" : 30,
            "state" : self.loop_coil_sensor_1.get_detected(),
            "available" : self.loop_coil_sensor_1.get_status()
        }
        state_message = json.dumps(state)
        self.publisher.publish("monitoring/loop_coil_1_sensor", state_message)

        state = {
            "pos" : "바닥센서_" + self.pos + "_2",
            "cpu" : 0.7,
            "ram" : 0.5,
            "temperature" : 30,
            "state" : self.loop_coil_sensor_2.get_detected(),
            "available" : self.loop_coil_sensor_2.get_status()
        }
        state_message = json.dumps(state)
        self.publisher.publish("monitoring/loop_coil_2_sensor", state_message)


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
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                ("monitoring", 0)
            ],
        }

    ex = LoopCoilSensorServer(config=config, pos=pos)
    ex.start()
    


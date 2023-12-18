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

class CrossingGateProgram(Program):
    def __init__(self, config, pos):
        self.config = config
        self.pos = pos

        if "입차" in self.pos:
            # 입차의 경우 in topic을 subscribe
            self.topic_dispatcher = {
                "hardware/server/crossing_gate/in/to": self.handle_in,
                "monitoring": self.handle_monitoring
            }
        elif "출차" in self.pos:
            # 출차의 경우 out topic을 subscribe
            self.topic_dispatcher = {
                "hardware/server/crossing_gate/out/to": self.handle_out,
                "monitoring": self.handle_monitoring
            }

        self.crossing_gate = CrossingGate(pos)
        self.log_publisher = MQTTclient.LogPublisher()
        self.demo_publisher = MQTTclient.DemoPublisher()

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        pass

    def handle_in(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        if data == 'open':
            # in / open
            self.crossing_gate.open()
        else:  
            # in / close
            self.crossing_gate.close()
        log = f"[차단기_{self.pos}] (상태: {self.crossing_gate.get_opened()})"
        self.log_publisher.log(log)
        self.demo_publisher.demo_print(log)


    def handle_out(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        if data == 'open':
            # out / open
            self.crossing_gate.open()
        else: 
            # out / close
            self.crossing_gate.close()
        log = f"[차단기_{self.pos}] (상태: {self.crossing_gate.get_opened()})"
        self.log_publisher.log(log)
        self.demo_publisher.demo_print(log)

    # topics에 ("monitoring", 0) 추가
    # topic_dispatcherd에 "monitoring" : self.handle_monitoring 추가
    def handle_monitoring(self, topic, data, publisher):
        state = {
            "cpu" : 0.7,
            "ram" : 0.5,
            "temperature" : 30,
            "state" : self.crossing_gate.get_opened(),
            "available" : self.crossing_gate.get_status(),
            "direction" : self.pos,
        }
        state_message = json.dumps(state)
        self.publisher.publish("monitoring/crossing_gate", state_message)

        

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
    
    if "입차" in pos:
        topic = "hardware/server/crossing_gate/in/to"
    else:
        topic = "hardware/server/crossing_gate/out/to"

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": port, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (topic, 0), 
                ("monitoring", 0)
            ],
        }

    ex = CrossingGateProgram(config=config, pos=pos)
    ex.start()
    


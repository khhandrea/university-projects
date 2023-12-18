import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hardware
import MQTTclient

from program import Program
import json, argparse
import datetime
from pyprnt import prnt



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


class DisplayProgram(Program):
    def __init__(self, config, pos):
        self.config = config
        self.pos = pos

        if "입차" in self.pos:
            # 입차의 경우 in topic을 subscribe
            topic_dispatcher = {
                "hardware/server/display/in/to": self.handle_display,
                "monitoring" : self.handle_monitoring,
            }
        elif "출차" in self.pos:
            # 출차의 경우 out topic을 subscribe
            topic_dispatcher = {
                "hardware/server/display/out/to": self.handle_display,
                "monitoring" : self.handle_monitoring,
            }

        self.topic_dispatcher = topic_dispatcher

        self.display = hardware.Display(pos=self.pos)

        self.log_publisher = MQTTclient.LogPublisher()
        self.demo_publisher = MQTTclient.DemoPublisher()

        super().__init__(self.config, self.topic_dispatcher)

    def get_time_stamp(self):
        current_time = datetime.datetime.today() # 2021-08-15 20:58:43.302125
        current_time =  current_time.strftime('%Y%m%d-%H%M%S') # 20210815205827

        return current_time

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        pass

    
    # TODO 각자에 맞게 추가하면 됨
    def handle_display(self, topic, data, publisher):        
        data = json.loads(data)

        cost: int = data["cost"]
        dis_cost: int = data["dis_cost"]
        car_num: int = data["car_num"]
        in_time: str = data["in_time"]
        out_time: str = data["out_time"]

        log = self.display.display_print(cost=cost, dis_cost=dis_cost, car_num=car_num, in_time=in_time, out_time=out_time)
        self.log_publisher.log(log)
        self.demo_publisher.demo_print(log)

    # topics에 ("monitoring", 0) 추가
    # topic_dispatcherd에 "monitoring" : self.handle_monitoring 추가
    def handle_monitoring(self, topic, data, publisher):
        state = {
            "cpu" : 0.7,
            "ram" : 0.5,
            "temperature" : 30,
            "state" : "None",
            "available" : self.display.get_status()
        }
        state_message = json.dumps(state)
        self.publisher.publish("monitoring/display", state_message)

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
        topic = "hardware/server/display/in/to"

    elif "출차" in pos:
        topic = "hardware/server/display/out/to"
    
    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": port, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                (topic, 0), 
                ("monitoring", 0),
            ],
        }

    display_program = DisplayProgram(config=config, pos=pos)
    display_program.start()
    


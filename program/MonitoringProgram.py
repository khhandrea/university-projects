import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from program import Program
import argparse, json
import datetime, time
from pyprnt import prnt
from queue import Queue
from threading import Semaphore

screen_lock = Semaphore(value=1)

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

monitoring_queue = Queue()


class MonitoringProgram(Program):
    def __init__(self, config):
        self.config = config

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            "monitoring/loop_coil_1_sensor" : self.handle_monitoring,
            "monitoring/loop_coil_2_sensor" : self.handle_monitoring,
            "monitoring/camera" : self.handle_monitoring,
            "monitoring/crossing_gate" : self.handle_monitoring,
            "monitoring/display" : self.handle_monitoring,
        }
        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

    def get_time_stamp(self):
        current_time = datetime.datetime.today() # 2021-08-15 20:58:43.302125
        current_time =  current_time.strftime('%Y%m%d-%H%M%S') # 20210815205827

        return current_time

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            event = input(">>>이벤트 입력: ")

            if event == "모니터링":
                # self.monitoring_state = {"pay_module": {}, "car_recog_server": {}, "crossing_gate_server": {}, "display_server": {}, "loop_coil_server": {}}

                self.publisher.publish("monitoring", "")
            time.sleep(2)

                


    
    # TODO 각자에 맞게 추가하면 됨
    def handle_monitoring(self, topic, data, publisher):
        # if "paymodule" in topic:
        #     self.monitoring_state["pay_module"] = json.loads(data)

        # elif "car_recog" in topic:
        #     self.monitoring_state["car_recog_server"] = json.loads(data)

        # elif "crossing_gate" in topic:
        #     self.monitoring_state["crossing_gate_server"] = json.loads(data)

        # elif "display" in topic:
        #     self.monitoring_state["display_server"] = json.loads(data)

        # elif "loop_coil" in topic:
        #     self.monitoring_state["loop_coil_server"] = json.loads(data)

        # # monitoring이 다 모였으면 출력
        # if {} not in self.monitoring_state.values():
        monitoring_data = json.loads(data)
        screen_lock.acquire()
        print()
        prnt(monitoring_data)
        screen_lock.release()
        # monitoring_queue.put(monitoring_data)


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

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": port, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                ("monitoring/loop_coil_1_sensor", 0), 
                ("monitoring/loop_coil_2_sensor", 0), 
                ("monitoring/camera", 0), 
                ("monitoring/crossing_gate", 0), 
                ("monitoring/display", 0), 
            ],
        }

    monitoring_program = MonitoringProgram(config=config)
    monitoring_program.start()
    


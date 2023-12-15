import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from threading import Thread
from program import Program
import time, json
import datetime



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


class CrossingGateRemoteControlProgram(Program):
    def __init__(self, config, topic_dispatcher):
        self.config = config

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            "hardware/server/parkingDB/from": self.handle_parkingDB,
        }
        self.topic_dispatcher = topic_dispatcher

        self.queue = Queue()

        super().__init__(self.config, self.topic_dispatcher)

    def get_time_stamp(self):
        current_time = datetime.datetime.today() # 2021-08-15 20:58:43.302125
        current_time =  current_time.strftime('%Y%m%d_%H%M%S') # 20210815_205827

        return current_time


    def get_ip_port_from_name(self, name):
        message = {
            "type": "get", 
            "target": "remote", 
            "pk": {"crossing_gate_name": f"{name}"}, 
            "item": {}
            }
        
        self.publisher.publish("hardware/server/parkingDB/to", message)

        data = self.queue.get()

        if data != "{}":
            ip = data["ip"]
            port = int(data["port"])

            return ip, port

        else:
            return -1, -1
    
    def get_topic_from_name(self, name): # crossing gate에 보내지 않고 car_recog에 보냄
        if "입차" in name:
            return "hardware/server/loop_coil/in/1/to", "hardware/server/loop_coil/in/2/to"
        elif "출차" in name:
            return "hardware/server/loop_coil/out/1/to", "hardware/server/loop_coil/out/2/to"
        else:
            return -1

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            event = input(">>>이벤트 입력: ")

            if event == "원격 차단기 열기":
                name = input(">>>차단기 이름: ")
                time = float(input(">>>시간: "))

                first_coil_topic, second_coil_topic = self.get_topic_from_name(name)
                ip, port = self.get_ip_port_from_name(name)

                if ip == -1 and port == -1:
                    print("없는 차단기 입니다.")
                else:
                    config = {
                        "ip": f"{ip}", 
                        "port": port, 
                        "topics": [],
                    }

                    remote_publisher = MQTTclient.Publisher(config=config)

                    time_stamp = self.get_time_stamp()
                    remote_publisher.publish(first_coil_topic, f"{time_stamp}/True")

                    time.sleep(time)
                    print(f"{time}초 후..")

                    time_stamp = self.get_time_stamp()
                    remote_publisher.publish(first_coil_topic, f"{time_stamp}/False")
                    remote_publisher.publish(second_coil_topic, f"{time_stamp}/True")

                    time.sleep(0.5)

                    time_stamp = self.get_time_stamp()
                    remote_publisher.publish(second_coil_topic, f"{time_stamp}/False")

    
    # TODO 각자에 맞게 추가하면 됨
    def handle_parkingDB(self, topic, data, publisher):
        # data = 
        self.queue.put(data.decode())

if __name__ == '__main__':

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 1883, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
                ("hardware/server/parkingDB/from", 0), 
            ],
        }

    crossing_gate_remote_control_program = CrossingGateRemoteControlProgram(config=config)
    crossing_gate_remote_control_program.start()
    


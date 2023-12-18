import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient
from log_utility import make_log_data

from program import Program, DBRepository
import re, datetime, json



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
    def __init__(self, config):
        self.config = config
        self.pos = "remote"

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            
        }
        self.topic_dispatcher = topic_dispatcher

        self.log_publisher = MQTTclient.LogPublisher()
        self.demo_publisher = MQTTclient.DemoPublisher()
        self.parking_db = DBRepository(pos=self.pos, db_name="parkingDB")

        super().__init__(self.config, self.topic_dispatcher)

    def get_time_stamp(self):
        current_time = datetime.datetime.today() # 2021-08-15 20:58:43.302125
        current_time =  current_time.strftime('%Y%m%d_%H%M%S') # 20210815_205827

        return current_time


    def get_ip_port_from_name(self, name):
        query = {
            "pos": self.pos,
            "type": "get", 
            "target": "mqtt_server", 
            "pk": {"name": f"{name}"}, 
            "item": {}
            }
        
        query = json.dumps(query)
        data = self.parking_db.get(query)

        if data != None:
            _, ip, port = data[1:-1].split(", ")

            ip = ip.replace("'", "")
            port = int(port)

            return ip, port

        else:
            return -1, -1
        
    def send_log_message(self, location):
        message = f"[원격 차단기 프로그램] 원격 열림 이벤트 발생 ({location})"
        message_log = make_log_data(message)
        self.log_publisher.log(message_log)

        self.demo_publisher.demo_print(f"[원격 차단기 프로그램] 원격 열림 이벤트 발생 ({location})")

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            event = input(">>이벤트 입력: ")

            if event == "원격 차단기 열기":
                name = input(">>차단기 이름: ")
                assert re.fullmatch(r'(\w+_\w+_\w+)', name), 'Position does not match the required pattern. Position should be "str_str_str".'

                time = float(input(">>머무르는 시간: "))
                direction = "in" if "입차" in name else "out"

                self.send_log_message(name)

                ip, port = self.get_ip_port_from_name(name)

                if ip == -1 and port == -1:
                    print("없는 차단기 입니다.")
                else:
                    config = {
                        "ip": ip, 
                        "port": port, 
                    }

                    remote_publisher = MQTTclient.Publisher(config=config)

                    time_stamp = self.get_time_stamp()
                    remote_publisher.publish("remote", f"{time}/{direction}")


if __name__ == '__main__':

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 60106, 
            "topics": [ # (topic, qos) 순으로 넣으면 subcribe됨
            ],
        }

    crossing_gate_remote_control_program = CrossingGateRemoteControlProgram(config=config)
    crossing_gate_remote_control_program.start()
    


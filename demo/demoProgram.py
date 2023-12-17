import sys, os
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient

from queue import Queue
from program import Program
import time, datetime, re



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


class demoProgram(Program):
    def __init__(self, config):
        self.config = config

        # TODO 각자에 맞게 고치면 됨
        # topic: handler 순으로 추가하면 된다.
        # 원하는 topic에 해당하는 반응을 구현하면 됨
        topic_dispatcher = {
            
        }
        self.topic_dispatcher = topic_dispatcher

        self.MQTT_server_info = {
            "등록"   : 60406,
            "상허문" : 60606,
            "일감문" : 60706,
            "건국문" : 60806,
        }

        self.MQTT_hardware_topic = {
            "카메라" : "camera",
            "차단기" : "crossing_gate",
            "디스플레이" : "display",
            "바닥센서" : "loop_coil_sensor",
            "결제모듈" : "pay_module",
        }


        self.queue_msg = Queue()

        super().__init__(self.config, self.topic_dispatcher)

    def get_time_stamp(self):
        current_time = datetime.datetime.today() # 2021-08-15 20:58:43.302125
        current_time =  current_time.strftime('%Y%m%d_%H%M%S') # 20210815_205827

        return current_time

    # TODO set_car_image
    def car_enter_event(self):
        car_num = input(">>차량 번호: ")
        door_location = input(">>문 위치: ")
        assert door_location in self.MQTT_server_info, 'Invalid door location. Door location should be one of "등록", "상허문", "일감문" ,"건국문".'

        duration = input(">>머무르는 시간: ")
        assert duration.replace('.','',1).isdigit(), 'Duration should be shape of float.'
        duration = float(duration)


        

        config = {
            "ip": "127.0.0.1", 
            "port": self.MQTT_server_info[door_location], 
        }
        print("port:", self.MQTT_server_info[door_location])

        enter_publisher = MQTTclient.Publisher(config=config)
        enter_publisher.publish("demo/hardware/loop_coil_sensor/in/1/to/recognition", 'True')

        time.sleep(duration)

        enter_publisher.publish("demo/hardware/loop_coil_sensor/in/1/to/recognition", 'False')
        enter_publisher.publish("demo/hardware/loop_coil_sensor/in/2/to/recognition", 'True')

        time.sleep(0.5)

        enter_publisher.publish("demo/hardware/loop_coil_sensor/in/2/to/recognition", 'False')

    # TODO set_car_image
    def car_exit_event(self):
        car_num = input(">>차량 번호: ")
        door_location = input(">>문 위치: ")
        assert door_location in self.MQTT_server_info, 'Invalid door location. Door location should be one of "등록", "상허문", "일감문" ,"건국문".'

        duration = input(">>머무르는 시간: ")
        assert duration.replace('.','',1).isdigit(), 'Duration should be the shape of float.'
        duration = float(duration)

        config = {
            "ip": "127.0.0.1", 
            "port": self.MQTT_server_info[door_location], 
        }

        enter_publisher = MQTTclient.Publisher(config=config)
        enter_publisher.publish("demo/hardware/loop_coil_sensor/out/1/to/recognition", 'True')

        time.sleep(duration)

        enter_publisher.publish("demo/hardware/loop_coil_sensor/out/1/to/recognition", 'False')
        enter_publisher.publish("demo/hardware/loop_coil_sensor/out/2/to/recognition", 'True')

        time.sleep(0.5)

        enter_publisher.publish("demo/hardware/loop_coil_sensor/out/2/to/recognition", 'False')

    def car_register_event(self):
        car_num = input(">>차량 번호: ")

        # TODO Add assert
        car_cartegory = input(">>차량 구분: ")
    

        id = input(">>신원 id: ")
        assert id.isdigit(), 'Id should be the shape of integer.'
        id = float(id)

        config = {
            "ip": "127.0.0.1", 
            "port": "60406",
        }

        data = f"{car_num}/{car_cartegory}/{id}"

        enter_publisher = MQTTclient.Publisher(config=config)
        enter_publisher.publish("hardware/server/registerCarProgram/to", data) # TODO topic 환희랑 맞춰야함 
           
    def broken_event(self):
        pos = input(">>객체 이름: ")
        assert re.fullmatch(r'(\w+_\w+)|(\w+_\w+_\w+)|(\w+_\w+_\w+_\d+)', pos), 'Position does not match the required pattern. Position should be "str_str", "str_str_str", or "str_str_str_int".'

        if "등록" in pos:
            hardware_name, location = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_location = "register"

            topic = f"demo/hardware/{hardware_name}/{topic_location}/to/broken"

        elif "바닥센서" in pos:
            hardware_name, location, direction, num = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_direction = "in" if direction == "입차방향" else "out"

            topic = f"demo/hardware/{hardware_name}/{topic_direction}/{num}/to/broken"

        else:
            hardware_name, location, direction = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_direction = "in" if direction == "입차방향" else "out"

            topic = f"demo/hardware/{hardware_name}/{topic_direction}/to/broken"

        print(topic)
        print(config)
        broken_publisher = MQTTclient.Publisher(config=config)
        broken_publisher.publish(topic, '고장')


    def repair_event(self):
        pos = input(">>객체 이름: ")
        assert re.fullmatch(r'(\w+_\w+)|(\w+_\w+_\w+)|(\w+_\w+_\w+_\d+)', pos), 'Position does not match the required pattern. Position should be "str_str", "str_str_str", or "str_str_str_int".'

        if "등록" in pos:
            hardware_name, location = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_location = "register"

            topic = f"demo/hardware/{hardware_name}/{topic_location}/to/broken"

        elif "바닥센서" in pos:
            hardware_name, location, direction, num = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_direction = "in" if direction == "입차방향" else "out"

            topic = f"demo/hardware/{hardware_name}/{topic_direction}/{num}/to/broken"

        else:
            hardware_name, location, direction = pos.split("_")

            hardware_name = self.MQTT_hardware_topic[hardware_name]
            config = {
                "ip": "127.0.0.1", 
                "port": self.MQTT_server_info[location], 
            }
            topic_direction = "in" if direction == "입차방향" else "out"

            topic = f"demo/hardware/{hardware_name}/{topic_direction}/to/broken"

        repair_publisher = MQTTclient.Publisher(config=config)
        repair_publisher.publish(topic, '정상')

    # TODO 각자에 맞게 고치면 됨
    def start(self):
        while True:
            event = input(">>이벤트 입력: ")

            if event == "입차":
                self.car_enter_event()

            elif event == "출차":
                self.car_exit_event()

            elif event == "차량등록":
                self.car_register_event()

            elif event == "고장남":
                self.broken_event()

            elif event == "고쳐짐":
                self.repair_event()

if __name__ == '__main__':

    # TODO 각자에 맞게 고치면 됨
    config = {
            "ip": "127.0.0.1", 
            "port": 60506, 
            "topics": [],
        }

    demo_program = demoProgram(config=config)
    demo_program.start()
    


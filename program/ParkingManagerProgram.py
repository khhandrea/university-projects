import sys, os, time
from json import dumps

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import MQTTclient
 
from queue import Queue
from program import Program
from datetime import datetime, timedelta
from program import DBRepository

from program import make_log_data

import argparse

queue_from_parking_db = Queue()
queue_paymodule = Queue()
queue_disabled = Queue()
queue_in_duration = Queue()
queue_out_duration = Queue()

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
        self.start_time = 0
        self.topic_dispatcher = {
            'hardware/server/loop_coil/in/1/from': self.handle_loop_coil_in_1,
            'hardware/server/loop_coil/in/2/from': self.handle_loop_coil_in_2,
            'hardware/server/loop_coil/out/1/from': self.handle_loop_coil_out_1,
            'hardware/server/loop_coil/out/2/from': self.handle_loop_coil_out_2,
            'hardware/server/car_recog/in/from': self.handle_car_recog_in,
            'hardware/server/car_recog/out/from': self.handle_car_recog_out,
            'hardware/server/paymodule/from': self.handle_paymodule,
            'demo/in/duration': self.handle_in_duration,
            'demo/out/duration': self.handle_out_duration,
            'demo/out/disabled': self.handle_disabled,
            'remote': self.handle_remote,
        }

        self.parking_db = DBRepository(pos=self.pos, db_name="parkingDB")

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        while True:
            pass

    def handle_parkingDB(topic, data, publisher):
        print(f'got {data} to parkingDB')
        data = data.split("/")
        queue_from_parking_db.put(data)

    def handle_loop_coil_in_1(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        self.publisher.publish('hardware/server/car_recog/in/to', 'capture')
        
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

        start_time = time.time()

        publisher.publish('hardware/server/crossing_gate/in/to', 'open')
        
        # recognition DB에 추가
        message = {
            'type': 'insert',
            'pos': self.pos,
            'target': 'recognition',
            'item': {
                'car_number': data.split('/')[1],
                'time': data.split('/')[0]
            }
        }
        message = dumps(message)
        self.parking_db.insert(message)

        end_time = time.time()
        time.sleep(max(0, queue_in_duration.get() - (end_time - start_time)))
        # loop coil 2 가동
        self.publisher.publish("demo/hardware/loop_coil_sensor/in/1/to/recognition", 'False')
        self.publisher.publish("demo/hardware/loop_coil_sensor/in/2/to/recognition", 'True')

        time.sleep(0.5)

        self.publisher.publish("demo/hardware/loop_coil_sensor/in/2/to/recognition", 'False')

    def handle_car_recog_out(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")

        start_time = time.time()

        # log = f"[{self.pos}_차량인식서버_출차방향] 차랑 번호 인식 이벤트 발생 (차량 번호: {self.car_num})"
        # self.publisher.publish("hardware/server/logDB/to", make_log_data(log))
        self.out_time, self.car_num = data.split('/')

        # 로그 불러오기 (입차 시간)
        query = {
            'type': 'get',
            'pos' : self.pos,
            'target': 'recognition',
            'pk': {
                'car_number': self.car_num
            }
        }
        query = dumps(query)
        recognition_info = self.parking_db.get(query)
        if recognition_info == "None":
            in_time = self.out_time
        else:
            _, in_time = recognition_info[1:-1].split(", ")
            in_time = in_time[1:-1]
        # 요금 계산
        start_date = datetime.strptime(in_time, "%Y%m%d_%H%M%S").date()
        flag = start_date
        end_date = datetime.strptime(self.out_time, "%Y%m%d_%H%M%S").date()
        cost, dis_cost = 0, 0
        while flag <= end_date:
            if flag == start_date:
                temp_in_time = self.str_to_time(in_time)
            else:
                temp_in_time = 0
            if flag == end_date:
                temp_out_time = self.str_to_time(self.out_time)
            else:
                temp_out_time = 86400
            time_min = (temp_out_time - temp_in_time)//60
            if time_min <= 15:
                cost += 0
            elif time_min <= 30:
                cost += 1500
            else:
                # 최초 30분까지는 1,500원
                # 이후 10분 당 500원
                # 1일 최고 30,000원
                cost += min(1500 + (time_min - 30)//10 * 500, 30000)
                # 장애인 차량 여부 확인 (입력)
            flag += timedelta(days=1)
            
        disabled = queue_disabled.get()
        if disabled:
            dis_cost = cost//2
            cost -= dis_cost

        # 등록 여부 확인 (정기권 차량)
        query = {
            'type': 'get',
            'pos' : self.pos,
            'target': 'register',
            'pk': {
                'car_number': self.car_num
            }
        }
        query = dumps(query)
        register_info = self.parking_db.get(query)
        if register_info != "None":
            dis_cost = cost
            cost -= dis_cost

        # display에 출력
        message = {
            'cost': cost,
            'dis_cost': dis_cost,
            'car_num': self.car_num,
            'in_time': in_time,
            'out_time': self.out_time
        }
        message = dumps(message)
        publisher.publish('hardware/server/display/out/to', message)

        while cost>0:
            # 결제 수단 요청 (입력) # 0원 초과일 경우에만
            publisher.publish('hardware/server/paymodule/to', f"{self.pos}/{cost}")
            is_pay_complete = queue_paymodule.get()

            if is_pay_complete:
                break
        
        publisher.publish('hardware/server/crossing_gate/out/to', 'open')

        # DB에서 제거
        message = {
            'type': 'delete',
            'pos': self.pos,
            'target': 'recognition',
            'pk':{
                'car_number': self.car_num
            }
        }
        message = dumps(message)
        self.parking_db.delete(message)

        end_time = time.time()
        time.sleep(max(0, queue_out_duration.get() - (end_time - start_time)))
        # loop coil 2 가동
        self.publisher.publish("demo/hardware/loop_coil_sensor/out/1/to/recognition", 'False')
        self.publisher.publish("demo/hardware/loop_coil_sensor/out/2/to/recognition", 'True')

        time.sleep(0.5)

        self.publisher.publish("demo/hardware/loop_coil_sensor/out/2/to/recognition", 'False')
    
    def handle_paymodule(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        # 성공했을 시, 문 열기
        result = True if "True" in data else False
        print("here is handle_paymodule")
        print(result)
        queue_paymodule.put(result)

    def handle_in_duration(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        queue_in_duration.put(float(data))

    def handle_out_duration(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        queue_out_duration.put(float(data))

    def handle_disabled(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        result = True if "예" in data else False
        queue_disabled.put(result)

    def handle_remote(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        duration, direction = data.split('/')
        # 차단기 열기
        publisher.publish(f'hardware/server/crossing_gate/{direction}/to', 'open')

        # duration만큼 기다리기
        time.sleep(float(duration))

        # loop coil 2 가동
        publisher.publish(f'hardware/server/crossing_gate/{direction}/to', 'close')

    def str_to_time(self, t):
        cur_time = datetime.strptime(t, "%Y%m%d_%H%M%S")
        m = cur_time.hour * 3600 + cur_time.minute * 60 + cur_time.second
        return m


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
                ('hardware/server/paymodule/from', 0),
                ('demo/in/duration', 0),
                ('demo/out/duration', 0),
                ('demo/out/disabled', 0),
                ('remote', 0), 
            ],
        }
    
    ex = ParkingManagerProgram(config=config, pos=pos)
    ex.start()
    


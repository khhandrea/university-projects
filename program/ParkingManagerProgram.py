import sys, os
from json import dumps

import MQTTclient
 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from queue import Queue
from program import Program
from datetime import datetime
import program.DBRepository import DBRepository

from program import make_log_data

import argparse

queue_from_parking_db = Queue()

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
            'hardware/server/paymodule/out/from': self.handle_paymodule
        }

        self.parking_db = DBRepository(pos=self.pos, db_name="parkingDB")

        super().__init__(self.config, self.topic_dispatcher)

    def start(self):
        pass

    def handle_parkingDB(topic, data, publisher):
        print(f'got {data} to parkingDB')
        data = data.split("/")
        queue_from_parking_db.put(data)

    def handle_loop_coil_in_1(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        publisher.publish('hardware/server/car_recog/in/to', 'capture')
        
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
        
        # recognition DB에 추가
        message = {
            'type': 'insert',
            'pos': self.pos,
            'target': 'recognition',
            'item': {
                'car_num': data.split('/')[1],
                'time': data.split('/')[0]
            }
        }
        message = dumps(message).encode('euc-kr')
        self.parking_db.insert(message)

    def handle_car_recog_out(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        # log = f"[{self.pos}_차량인식서버_출차방향] 차랑 번호 인식 이벤트 발생 (차량 번호: {self.car_num})"
        # self.publisher.publish("hardware/server/logDB/to", make_log_data(log))
        self.out_time, self.car_num = data.split('/')

        # 로그 불러오기 (입차 시간)
        recognition_info = self.request_recognition_info(self.car_num)
        if recognition_info == None:
            in_time = self.out_time
        else:
            _, in_time = recognition_info
        # 요금 계산
        time_min = (self.str_to_sec(self.out_time) - self.str_to_sec(in_time))//60
        if time_min <= 15:
            cost = 0
            dis_cost = 0
        elif time_min <= 30:
            cost = 1500
            dis_cost = 0
        else:
            # 최초 30분까지는 1,500원
            # 이후 10분 당 500원
            # 1일 최고 30,000원

            cost = min(1500 + (time_min - 30)//10 * 500, 30000)
            dis_cost = 0
            # 장애인 차량 여부 확인 (입력)
            disabled = input(">>장애인 차량 여부(yes, no) :")
            if disabled == "yes":
                dis_cost = cost//2
                cost -= dis_cost

        # 등록 여부 확인 (정기권 차량)
        query = {
            'type': 'get',
            'target': 'register',
            'pk': {
                'car_num': self.car_num
            }
        }
        query = dumps(query).encode('euc-kr')
        register_info = self.parking_db.get(query)
        if register_info != None:
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
        publisher.publish('hardware/server/display/out/to', message)

        if cost>0:
            # 결제 수단 요청 (입력) # 0원 초과일 경우에만
            bill_method = input()# TODO
            if bill_method == 'card':
                card_number = 1234567890123333
                cash_billed = 0
            elif bill_method == 'cash':
                card_number = None
                cash_billed = 40000
            # 결제 모듈 (요청)
            publisher.publish('hardware/server/paymodule/out/to', f"{cost}/{bill_method}/{card_number}/{cash_billed}")

        # DB에서 제거
        message = {
            'type': 'delete',
            'pos': self.pos,
            'target': 'recognition',
            'pk':{
                'car_num': self.car_num
            }
        }
        message = dumps(message).encode('euc-kr')
        self.parking_db.delete(message)
    
    def handle_paymodule(self, topic, data, publisher):
        print(f"topic: {topic}")
        print(f"data: {data}")
        # 성공했을 시, 문 열기
        if "True" in data:
            publisher.publish('hardware/server/crossing_gate/out/to', 'open')
            self.out_time, self.car_num = "", ""
        else:
            publisher.publish('hardware/server/car_recog/out/from', self.out_time+"/"+self.car_num)

    def str_to_sec(self, t):
        # month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # # YYMMDD_HHmmSS -> min
        # m = int(t[0:2]) - 1
        # m = m*365 + month_days[:int(t[2:4])].sum()
        # m += int(t[4:6]) - 1
        # m = m * 24 + int(t[7:9])
        m = int(t[7:9])
        m = m * 60 + int(t[9:11])
        m = m * 60 + int(t[11:13])
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
                ('hardware/server/paymodule/out/from', 0)
            ],
        }
    
    ex = ParkingManagerProgram(config=config, pos=pos)
    ex.start()
    


import sys
from os.path import dirname, abspath
from json import dumps
from queue import Queue
 
sys.path.append(dirname(abspath(dirname(__file__))))
import argparse
from program import Program
from program import make_log_data
from MQTTclient import LogPublisher

queue = Queue()

class PayProgram(Program):
    def __init__(self, config, topic_dispatcher, pos):
        self.config = config
        self.topic_dispatcher = topic_dispatcher
        self.log_publisher = LogPublisher()

        super().__init__(self.config, self.topic_dispatcher)

    def pay(self, price: int):
        complete = False
        change = 0

        print(f'결제 {price}원 내야 합니다.')
        pay_method = input('결제 수단: ')

        if pay_method == 'card' or pay_method == '카드':
            pay_info = int(input('카드 번호: '))
            pay_info_name = '카드 번호'
            complete = True
        else: # cash
            pay_info = int(input('금액: '))
            pay_info_name = '현금'
            if pay_info >= price:
                complete = True
            change = pay_info - price

        log = f"[결제모듈_{pos}] 결제 이벤트 발생 (가격: {price}, 방법: {pay_method}, {pay_info_name}: {pay_info}"
        message = '/'.join((str(complete), str(change)))
        return message, log

    def start(self):
        while True:
            pos, price = queue.get()
            message, log = self.pay(price)
            data = {
                'type': 'insert',
                'target': 'log',
                'item': {
                    'message': log
                }
            }
            data = dumps(data)

            self.log_publisher.log(data)
            self.publisher.publish("hardware/server/paymodule/from", message)

def handle_payment(topic, data, publisher):
    data = data.split('/')
    data[1] = int(data[1])
    queue.put(data)

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
    elif pos == '차량등록서버':
        port = 60406
    else:
        raise ValueError("Wrong position")
    
    print(port)

    config = {
            "ip": "127.0.0.1", 
            "port": port, 
            "topics": [
                ("hardware/server/paymodule/to", 0),
            ],
        }
    
    topic_dispatcher = {
        "hardware/server/paymodule/to": handle_payment,
    }

    pay_program = PayProgram(config=config, topic_dispatcher=topic_dispatcher, pos=pos)
    pay_program.start()
    


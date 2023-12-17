import argparse
import sys
from os.path import dirname, abspath
from queue import Queue
 
sys.path.append(dirname(abspath(dirname(__file__))))
from program import Program
from program import make_log_data

queue = Queue()

class PayProgram(Program):
    def __init__(self, config, topic_dispatcher, pos):
        self.config = config
        self.topic_dispatcher = topic_dispatcher

        super().__init__(self.config, self.topic_dispatcher)

    def pay(self, price: int, pay_method: str, card_num: int, cash_billed: int):
        complete = False
        change = 0

        if pay_method == 'card':
            complete = True
        else: # cash
            if cash_billed >= price:
                complete = True
            change = cash_billed - price

        log = f"[결제모듈_{pos}] 결제 이벤트 발생 (가격: {price}, 방법: {pay_method}, 카드번호: {card_num}, 현금: {cash_billed})"
        message = '/'.join((str(complete), str(change)))
        return message, log

    def start(self):
        while True:
            if not queue.empty():
                price, pay_method, card_num, cash_billed = queue.get()
                message, log = self.pay(price, pay_method, card_num, cash_billed)

                print(log, message)
                self.publisher.publish("hardware/server/logDB/to", make_log_data(log))
                self.publisher.publish("hardware/server/paymodule/from", message)

def handle_payment(topic, data, publisher):
    data = data.split('/')
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
    else:
        raise ValueError("Wrong position")

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
    


from interface.DisplayInterface import DisplayInterface
import demo
from datetime import datetime

class Display(DisplayInterface):
    def __init__(self, pos):
        self._pos = pos
        self._status = '정상'
        self.demo_program = demo.DemoDisplayProgram(self)

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')

    def display_print(self, cost: int, dis_cost: int, car_num: int, in_time: str, out_time: str):
        if self._status != "고장":
            message = f'[디스플레이_{self._pos}]\n-차량 번호:{car_num}\n-입차 시간:{self.str_format(in_time)}\n-출차 시간:{self.str_format(out_time)}\n-이용 금액:{cost+dis_cost}원\n-할인된 금액:{dis_cost}원\n-결제할 금액:{cost}원'
            return message
        else:
            message = f'[디스플레이_{self._pos}]\ndisplay 고장'
        return message
    
    def str_format(self, time_str):
        t = datetime.strptime(time_str, "%Y%m%d_%H%M%S")
        return f"{t.year}월 {t.month}월 {t.day}일 {t.hour}시 {t.minute}분 {t.second}초"
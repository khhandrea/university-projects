from interface.DisplayInterface import DisplayInterface
class Display(DisplayInterface):
    def __init__(self, pos):
        self._pos = pos
        self._status = '정상'

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')

    def print(self, cost: int, dis_cost: int, car_num: int, in_time: str, out_time: str):
        print(f'차량 번호 : {car_num}')
        print(f'입차 시간 : {in_time}')
        print(f'출차 시간 : {out_time}')
        print(f'이용 금액 : {cost+dis_cost}원')
        print(f'할인된 금액 : {dis_cost}원')
        print(f'결제할 금액 : {cost}원')
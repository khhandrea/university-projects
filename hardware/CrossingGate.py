from interface.CrossingGateInterface import CrossingGateInterface
import demo

class CrossingGate(CrossingGateInterface):
    def __init__(self, pos):
        self._pos = pos # posiiton of device
        self._status = '정상'
        self._opened = '닫힘'
        self.demo_program = demo.DemoCrossingGateProgram(self)

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')

    def open(self):
        if self._status != "고장":
            self._opened = '열림'

    def close(self):
        if self._status != "고장":
            self._opened = '닫힘'

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status
    
    def get_opened(self):
        return self._opened
    
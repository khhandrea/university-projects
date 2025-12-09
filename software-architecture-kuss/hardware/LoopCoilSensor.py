from interface.LoopColiSensorInterface import LoopCoilSensorInterface
from state import LoopCoilBrokenState, LoopCoilStandardState
import demo

class LoopCoilSensor(LoopCoilSensorInterface):
    def __init__(self, pos):
        self._pos = pos
        self._status = '정상'
        self._state = LoopCoilStandardState()
        self._detected = False
        self.demo_program = demo.DemoLoopCoilSensorProgram(self)

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status
    
    def set_state(self, state):
        print(state)
        self._state = state
    
    def get_detected(self):
        return self._detected

    # for demo
    def set_detected(self, detected):
        return self._state.action(self, detected)

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')


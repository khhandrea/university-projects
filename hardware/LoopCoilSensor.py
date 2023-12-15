from interface.LoopColiSensorInterface import LoopCoilSensorInterface
from LoopCoil import LoopCoil

class LoopCoilSensor(LoopCoilSensorInterface):
    def __init__(self, pos):
        self._pos = pos
        self._status = '정상'
        self._loop_coil = LoopCoil()

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status
    
    def get_loop_coil(self):
        return self._loop_coil

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')
    
    def signal(self):
        # TODO: get signal from self.loop_coil
        car_pass = False
        return car_pass

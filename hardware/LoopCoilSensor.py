from interface.LoopColiSensorInterface import LoopCoilSensorInterface
from LoopCoil import LoopCoil

class LoopCoilSensor(LoopCoilSensorInterface):
    def __init__(self, pos):
        self.pos = pos
        self.status = '정상'
        self.loop_coil = LoopCoil()

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self.status}')
        self.status = status
        print(f'변경 상태 : {self.status}')

    def get_status(self):
        return self.status
    
    def signal(self):
        # TODO: get signal from self.loop_coil
        car_pass = False
        return car_pass

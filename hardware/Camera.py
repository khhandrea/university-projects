from interface.CameraInterface import CameraInterface
import demo

class Camera(CameraInterface):
    def __init__(self, pos):
        self._pos = pos # posiiton of device
        self._status = '정상'
        self.demo_program = demo.DemoCameraProgram(self)

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self.status}')
        self.status = status
        print(f'변경 상태 : {self.status}')

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status

    def capture(self):
        # TODO implement image
        image = ['12가1235']
        return image
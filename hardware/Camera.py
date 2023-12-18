from interface.CameraInterface import CameraInterface
import demo

class Camera(CameraInterface):
    def __init__(self, pos):
        self._pos = pos # posiiton of device
        self._status = '정상'
        self.demo_program = demo.DemoCameraProgram(self)
        self.image = ['12가1235']

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self.status}')
        self.status = status
        print(f'변경 상태 : {self.status}')

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status
    
    def set_image(self, image):
        print('set image 불림')
        self.image = image

    def capture(self):
        if self._status == '고장':
            return None
        return self.image
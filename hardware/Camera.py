from interface.CameraInterface import CameraInterface

class Camera(CameraInterface):
    def __init__(self, pos):
        self.pos = pos # posiiton of device
        self.status = '정상'

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self.status}')
        self.status = status
        print(f'변경 상태 : {self.status}')

    def capture(self):
        # TODO implement image
        image = []
        return image
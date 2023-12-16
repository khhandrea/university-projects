from interface.PayModuleInterface import PayModuleInterface
from hardware.PayMethod import PayMethod
from demo import PayModuleProgram

class PayModule(PayModuleInterface):
    def __init__(self, pos):
        self._pos = pos
        self._status = '정상'
        self.demo_program = PayModuleProgram(self)

    def get_pos(self):
        return self._pos
    
    def get_status(self):
        return self._status

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self._status}')
        self._status = status
        print(f'변경 상태 : {self._status}')

    def pay(self, cost: int, method: PayMethod):
        # TODO : implement pay
        pass

    def process_pay(self, cost: int, method: PayMethod):
        # TODO : implement proess_pay
        pass
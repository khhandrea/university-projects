from interface.PayModuleInterface import PayModuleInterface
from hardware.PayMethod import PayMethod

class PayModule(PayModuleInterface):
    def __init__(self, pos):
        self.pos = pos
        self.status = '정상'

    def set_status(self, status):
        assert status == '정상' or status == '고장'

        print(f'현재 상태 : {self.status}')
        self.status = status
        print(f'변경 상태 : {self.status}')

    def pay(self, cost: int, method: PayMethod):
        # TODO : implement pay
        pass

    def process_pay(self, cost: int, method: PayMethod):
        # TODO : implement proess_pay
        pass
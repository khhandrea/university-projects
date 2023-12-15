from hardware.PayMethod import PayMethod

class Card(PayMethod):
    def __init__(self, type, number, balance):
        super().__init__(balance)
        self.type = type
        self._number = number

    def get_number(self):
        return self._number
     
    def get_balance(self):
        return self._balance

    def pay(self, cost):
        #TODO: implement pay (calculate balance)
        pass

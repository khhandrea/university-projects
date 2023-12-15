from hardware.PayMethod import PayMethod

class Card(PayMethod):
    def __init__(self, type, number, balance):
        super().__init__(balance)
        self.type = type
        self.number = number

    def get_number(self):
        return self.number
    
    def pay(self, cost):
        #TODO: implement pay (calculate balance)
        pass
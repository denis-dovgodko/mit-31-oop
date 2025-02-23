from home_ownership import HomeOwnership
from datetime import datetime

class SingleOwnership(HomeOwnership):
    def __init__(self, address: str, owner: str):
        HomeOwnership.__init__(self, address)
        self.__owner = owner
        self.__to_pay = 0

    @property
    def owner(self):
        return self.__owner
    
    def submit_meter_readings(self, gas_used, submitter):
        if self.__owner == submitter and self.month != datetime.now().strftime("%B"):
            self.gas_previous = self.gas_current
            self.gas_current += gas_used
            self.__to_pay += self.gas_price * (self.gas_current - self.gas_previous)
            self.month = datetime.now().strftime("%B")
        return print(f'{datetime.now().strftime("%B"):}: Current meter {self.gas_current}, ${self.__to_pay} to pay')

    def pay(self, desired_total):
        self.__to_pay -= desired_total
        return print(f'Succeed transaction, now your bill is {self.__to_pay}')
   
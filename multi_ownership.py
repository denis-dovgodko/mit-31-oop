from datetime import datetime
from home_ownership import HomeOwnership

class MultiOwnership(HomeOwnership):
    def __init__(self, address: str, owners: dict):
        HomeOwnership.__init__(self, address)
        self.__owners = owners
        self.__owners_bills = {owner: 0 for owner in self.__owners.keys()}
        self.__calculate_living_total()

    def submit_meter_readings(self, gas_used, submitter):
        if self.__owners.get(submitter) is not None and self.month != datetime.now().strftime("%B"):
            self.gas_previous = self.gas_current
            self.gas_current += gas_used
            bill = self.gas_price * (self.gas_current - self.gas_previous)
            bill_per_one = bill / self.__living_total
            for owner_name in self.__owners.keys():
                bill_for_living = bill_per_one*self.__owners.get(owner_name)
                self.__owners_bills.update({owner_name: bill_for_living})
                print(f'Owner {owner_name}, {self.__owners.get(owner_name)} livings. Total: ${bill_for_living}')
            self.month = datetime.now().strftime("%B")
        return print(f'{datetime.now().strftime("%B"):}: Current meter {self.gas_current}, total ${bill} to pay, ${bill_per_one}',
                     'for one living')
    
    def pay(self, desired_total, submitter):
        if self.__owners.get(submitter) is not None:
            bill = self.__owners_bills.get(submitter)
            self.__owners_bills.update({submitter: bill-desired_total})
            return print(f'Succeed transaction, now your bill is {self.__owners_bills.get(submitter)}')
        print('Something went wrong')

    def __calculate_living_total(self):
        self.__living_total = sum(self.__owners.get(owner) for owner in self.__owners.keys())

    def add_owner(self, owner: dict):
        self.__owners.update(owner)
        self.__owners_bills.update({owner_name: 0 for owner_name in owner})
        self.__calculate_living_total()

    def delete_owner(self, owner_name):
        self.__owners.pop(owner_name)
        self.__owners_bills.pop(owner_name)
        self.__calculate_living_total()

    def change_owner(self, owner: dict):
        self.add_owner(owner)
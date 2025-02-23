from abc import abstractmethod, ABCMeta
from consumers import Consumers

class HomeOwnership(metaclass=ABCMeta):
    __gas_price = 12
    def __init__(self, address):
        self.__address = address
        self.__gas_current = 0
        self.__gas_previous = 0
        self.__month = "December"
        consumers.append(self)

    @property
    def address(self):
        return self.__address
    
    @property
    def gas_current(self):
        return self.__gas_current
    
    @property
    def gas_previous(self):
        return self.__gas_previous
    
    @property
    def gas_price(self):
        return self.__gas_price
    
    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self, month):
        self.__month = month

    @gas_current.setter
    def gas_current(self, gas_current):
        self.__gas_current = gas_current

    @gas_previous.setter
    def gas_previous(self, gas_previous):
        self.__gas_previous = gas_previous

    @abstractmethod
    def submit_meter_readings(self, gas_used):
        pass

    @abstractmethod
    def pay(self, desired_total):
        pass    
        
consumers = Consumers()
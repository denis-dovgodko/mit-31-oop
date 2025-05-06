# Visitor template
from __future__ import annotations
from abc import ABC, abstractmethod
from threading import Thread
from typing import List

class Car(ABC):
    @abstractmethod
    def ride(self):
        pass

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_car_tesla(self, element: ConcreteCarTesla) -> None:
        pass
    @abstractmethod
    def visit_concrete_car_audi(self, element: ConcreteCarAudi) -> None:
        pass

class ConcreteCarTesla(Car):
    def ride(self, visitor: Visitor) -> None:
        visitor.visit_concrete_car_tesla(self)

    def autopilot_ride(self) -> str:
        return "driven by autopilot"
    
class ConcreteCarAudi(Car):
    def ride(self, visitor: Visitor) -> None:
        visitor.visit_concrete_car_audi(self)

    def sport_ride(self) -> str:
        return "sport ride mode"
    
class ConcreteVisitor1(Visitor):
    def visit_concrete_car_tesla(self, element) -> None:
        print(f"{element.autopilot_ride()} + ConcreteVisitor1")

    def visit_concrete_car_audi(self, element) -> None:
        print(f"{element.sport_ride()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_car_tesla(self, element) -> None:
        print(f"{element.autopilot_ride()} + ConcreteVisitor2")

    def visit_concrete_car_audi(self, element) -> None:
        print(f"{element.sport_ride()} + ConcreteVisitor2")


def client_code(cars: List[Car], visitor: Visitor) -> None:
    for car in cars:
        car.ride(visitor)

def multi_client_code(cars: List[Car], visitor: Visitor) -> None:
    threads = []
    for car in cars:
        thread = Thread(target=car.ride, args=(visitor,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    cars = [ConcreteCarTesla(), ConcreteCarAudi()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(cars, visitor1)
    multi_client_code(cars, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(cars, visitor2)
    multi_client_code(cars, visitor2)
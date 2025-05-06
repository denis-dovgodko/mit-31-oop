from models.entities import Company, Owner, CompanyList, OwnerList
from multipledispatch import dispatch
from models.repositories import JsonData
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, income: float, is_resident: bool) -> float:
        pass

class DefaultPaymentSystem(PaymentStrategy):
    def calculate_tax(self, income: float, is_resident: bool) -> float:
        if not is_resident:
            return 0.25 * income
        if 1 <= income < 10000:
            return 0.05 * income
        if 10001 <= income < 50000:
            return 0.1 * income
        elif 50001 <= income < 100000:
            return 0.15 * income
        elif 100001 <= income < 500000:
            return 0.2 * income
        elif 500001 <= income < 1000000:
            return 0.3 * income
        elif income > 1000000:
            return 0.45 * income
        return 0

class PaymentSystem:
    performed_payments = {} 
    total_payed_taxes = 0

    def __init__(self, strategy):
        self.strategy: DefaultPaymentSystem = strategy

    @dispatch(Company, int)
    def calculate_taxes(self, company: Company, year):
        profit = company.annual_profit.get(year)
        budget = company.paying_system * profit
        if profit != None:
            for owner in company.owners_percentage:
                percent = company.owners_percentage.get(owner)
                if PaymentSystem.verify_unpaid(owner, year):
                    self.pay(OwnerList.owners_dict.get(owner), year, percent, budget)

    @dispatch(Owner, int)
    def calculate_taxes(self, owner: Owner, year):
        target_company = None
        for company in CompanyList.companies:
            if CompanyList.companies_dict[company.name].owners.get(owner.name) is not None:
                target_company = company
                break
        self.calculate_taxes(target_company, year)

    @staticmethod
    def verify_unpaid(owner: Owner, year: int):
        if PaymentSystem.performed_payments.get(owner+str(year)) == None:
            return True
        return False

    def pay(self, owner: Owner, year: int, percent: float, budget: int):
        key = owner.name+str(year)
        income = percent * budget
        taxes = self.strategy.calculate_tax(income, owner.is_resident)
        PaymentSystem.total_payed_taxes += taxes
        payment = percent * budget - taxes
        PaymentSystem.save_taxes(key, payment)

    @staticmethod
    def save_taxes(payer: str, payment: int):
        PaymentSystem.performed_payments[payer] = payment
        print(PaymentSystem.performed_payments)
        print(PaymentSystem.total_payed_taxes)
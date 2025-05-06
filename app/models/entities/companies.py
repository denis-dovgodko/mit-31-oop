import zope.interface
from pathlib import Path
from typing import List
from interfaces import IEntitiesList
from models.repositories import *
from models.entities import OwnerList
from abc import ABC, abstractmethod

class ProfitCalculateStrategy(ABC):
    @abstractmethod
    def calculate(self, company: 'Company') -> float:
        pass
    
class DefaultProfitCalculateStrategy(ProfitCalculateStrategy):
    def calculate(self, company: 'Company') -> float:
        residents_count = sum(
            1 for owner in company.owners.keys()
            if OwnerList.owners_dict[owner].is_resident
        )
        owners_len = len(company.owners)
        ratio = residents_count/owners_len
        if ratio < 0.5:
            return 0.4
        elif ratio == 0.5:
            return 0.5
        else:
            return 0.6

class Company:
    def __init__(self, name: str, shares: int, strategy: DefaultProfitCalculateStrategy):
        self.name = name
        self.shares = shares
        self.owners = {}
        self.owners_percentage = {}
        self.annual_profit = {}
        self.paying_system = 0
        self.strategy = strategy
        CompanyList.add_entity(self) 

    def add_entity(self, ownername: str, shares_to_add: int):
        if self.get_total_shares() + shares_to_add > self.shares:
            raise ValueError("Shares sum must be less than 100%")
        self.owners[ownername] = shares_to_add
        for owner in self.owners.keys():
            self.owners_percentage[owner] = self.owners[owner]/self.shares
        self.define_paying_system()
        CompanyList.refresh()
    
    def get_total_shares(self):
        return sum(self.owners.values())
    
    def set_annual_profit(self, year: int, profit: float):
        self.annual_profit[year] = profit
        CompanyList.refresh()

    def define_paying_system(self):
        self.paying_system = self.strategy.calculate(self)

    def to_dict(self):
        return {
            "name": self.name,
            "shares": self.shares,
            "owners": self.owners,
            "owners_percentage": self.owners_percentage,
            "annual_profit": self.annual_profit,
            "paying_system": self.paying_system
        }

@zope.interface.implementer(IEntitiesList)
class CompanyList:
    path = "data/companies/registry"
    companies = []
    companies_dict = {}

    @staticmethod
    def add_entity(company: Company):
        CompanyList.companies_dict[company.name] = company
        CompanyList.companies.append(company)
        CompanyList.save()

    @staticmethod
    def sort():
        CompanyList.companies.sort(key=lambda company: company.name)

    @staticmethod
    def to_dict():
        return [company.to_dict() for company in CompanyList.companies]
    
    @staticmethod
    def save():
        CompanyList.sort()
        csv_repository.save_data(CompanyList.path, CompanyList.to_dict())
        json_repository.save_data(CompanyList.path, CompanyList.to_dict())
        yaml_repository.save_data(CompanyList.path, CompanyList.to_dict())

    @staticmethod
    def refresh():
        CompanyList.save()

import zope.interface
from pathlib import Path
from typing import List
from interfaces import IEntitiesList
from models.repositories import *
from models.entities import OwnerList

class Company:
    def __init__(self, name: str, shares: int):
        self.name = name
        self.shares = shares
        self.owners = {}
        self.owners_percentage = {}
        self.annual_profit = {}
        self.paying_system = 0
        CompanyList.add_entity(self) 

    def add_entity(self, ownername: str, shares_to_add: int):
        if self.get_total_shares() + shares_to_add > self.shares:
            raise ValueError("Shares sum must be less than 100%")
        self.owners[ownername] = shares_to_add
        for owner in self.owners.keys():
            self.owners_percentage[owner] = self.owners[owner]/self.shares
        Company.define_paying_system(self)
        CompanyList.refresh()
    
    def get_total_shares(self):
        return sum(self.owners.values())
    
    def set_annual_profit(self, year: int, profit: float):
        self.annual_profit[year] = profit
        CompanyList.refresh()

    @staticmethod
    def define_paying_system(company: 'Company'):
        residents_count = 0
        owners_len = len(company.owners.keys())
        for owner in company.owners.keys():
            if OwnerList.owners_dict[owner].is_resident:
                residents_count += 1
        if residents_count / owners_len < 0.5:
            company.paying_system = 0.4
        elif residents_count / owners_len == 0.5:
            company.paying_system = 0.5
        elif residents_count / owners_len > 0.5:
            company.paying_system = 0.6

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
        return [company.__dict__ for company in CompanyList.companies]
    
    @staticmethod
    def save():
        CompanyList.sort()
        csv_repository.save_data(CompanyList.path, CompanyList.to_dict())
        json_repository.save_data(CompanyList.path, CompanyList.to_dict())
        yaml_repository.save_data(CompanyList.path, CompanyList.to_dict())

    @staticmethod
    def refresh():
        CompanyList.save()

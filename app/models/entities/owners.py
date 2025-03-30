import zope.interface
from typing import List
from interfaces import IEntitiesList
from models.repositories import *

class Owner:
    def __init__(self, name: str, tax_id: int, is_resident: bool):
        self.name = name
        self.__tax_id = tax_id
        self.is_resident = is_resident
        OwnerList.add_entity(self) 

    @property
    def tax_id(self):
        return self.__tax_id
    
    @tax_id.setter
    def tax_id(self, value):
        self.__tax_id = value
        OwnerList.refresh()

@zope.interface.implementer(IEntitiesList)
class OwnerList:
    path = "data/owners/registry"
    owners = []
    owners_dict = {}

    @staticmethod
    def add_entity(owner: Owner):
        OwnerList.owners.append(owner)
        OwnerList.owners_dict[owner.name] = owner
        OwnerList.save()

    @staticmethod
    def sort():
        OwnerList.owners.sort(key=lambda owner: owner.tax_id)

    @staticmethod
    def to_dict():
        return [owner.__dict__ for owner in OwnerList.owners]

    # @staticmethod
    # def from_dict(data):
    #     OwnerList.owners = [Owner(**owner) for owner in data]

    @staticmethod
    def save():
        OwnerList.sort()
        csv_repository.save_data(OwnerList.path, OwnerList.to_dict())
        json_repository.save_data(OwnerList.path, OwnerList.to_dict())
        yaml_repository.save_data(OwnerList.path, OwnerList.to_dict())

    @staticmethod
    def refresh():
        OwnerList.save()

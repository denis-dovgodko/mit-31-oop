import zope.interface

class IEntitiesList(zope.interface.Interface):
    def add_entity():
        pass
    def sort():
        pass
    def to_dict():
        pass
    def save():
        pass
    def refresh():
        pass
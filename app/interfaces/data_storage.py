import zope.interface

class IData(zope.interface.Interface):
    def load_data(filename: str):
        pass
    def save_data(filename: str, data: dict):
        pass
    def find(filename: str, key: str, value):
        pass
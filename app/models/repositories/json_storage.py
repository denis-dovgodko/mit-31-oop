import zope.interface
import json
import os
from pathlib import Path
from interfaces import IData

@zope.interface.implementer(IData)
class JsonData:
    def load_data(self, filename: str):
        
        filename = Path(filename).with_suffix('.json')
        with open(filename, 'r') as file:
            return json.load(file)

    def save_data(self, filename: str, data: dict):
        filename = Path(filename).with_suffix('.json')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)

    def find(self, filename: str, key: str, value):
        filename = Path(filename).with_suffix('.json')
        data = self.load_data(filename)
        for obj in data:
            if dict(obj).get(key) == value:
                return obj

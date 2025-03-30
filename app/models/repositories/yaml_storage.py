import zope.interface
import yaml
import os
from pathlib import Path
from interfaces import IData

@zope.interface.implementer(IData)
class YamlData:
    def load_data(self, filename: str):
        filename = Path(filename).with_suffix('.yaml')
        with open(filename, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

    def save_data(self, filename: str, data: dict):
        filename = Path(filename).with_suffix('.yaml')
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

    def find(self, filename: str, key: str, value):
        filename = Path(filename).with_suffix('.yaml')
        data = self.load_data(filename)
        for obj in data:
            if dict(obj).get(key) == value:
                return obj
            

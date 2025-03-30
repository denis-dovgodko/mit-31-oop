import zope.interface
import csv
import os
from pathlib import Path
from interfaces import IData

@zope.interface.implementer(IData)
class CsvData:
    def load_data(self, filename: str):
        filename = Path(filename).with_suffix('.csv')
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def save_data(self, filename: str, data: list[dict]):
        filename = Path(filename).with_suffix('.csv')
        if not data:
            raise ValueError("Empty data")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    def find(self, filename: str, key: str, value):
        filename = Path(filename).with_suffix('.csv')
        data = self.load_data(filename)
        for obj in data:
            if dict(obj).get(key) == value:
                return obj

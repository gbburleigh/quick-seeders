import json
import os
import csv
from faker import Faker
from typing import Any, Dict, List, Union
from pathlib import Path

fake = Faker()

class Seeder:
    def __init__(self):
        self.fake = Faker()
        self.data = {}
        self.export_path = self.make_export_dir()

    def seed(self, schema: List[Any], count: int = 1) -> List[Dict[str, Any]]:
        result = []
        for _ in range(count):
            seed = {}
            for i in range(len(schema)):
                new = schema[i]()
                seed[new[1]] = new[0]
                del new
                
            result.append(seed)

        self.data = result
        return result

    def to_sql(self, filename: str, table: str) -> str:
        if self.data == {}:
            raise Exception("No data to export")
        with open(self.format_filename(filename) + '.sql', 'w') as f:
            columns = ', '.join(self.data[0].keys())
            sqlStr = f"INSERT INTO {table} ({columns}) VALUES "
            for row in self.data:
                values = ', '.join(f"'{value}'" for value in row.values())
                sqlStr += f"({values}), "
            sqlStr = sqlStr[:-2] + ';'
            f.write(sqlStr)

            return os.getcwd() + '/' + filename + '.sql'

    def to_json(self, filename: str) -> str:
        if self.data == {}:
            raise Exception("No data to export")
        with open(self.format_filename(filename) + '.json', 'w') as f:
            json.dump(self.data, f, indent=4)

            return os.getcwd() + '/' + filename + '.json'

    def to_csv(self, filename: str) -> str:
        if self.data == {}:
            raise Exception("No data to export")
        with open(self.format_filename(filename) + '.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.data[0].keys())
            for row in self.data:
                writer.writerow(row.values())

            return os.getcwd() + '/' + filename + '.csv'

    def make_export_dir(self):
        try:
            Path('exports').mkdir(parents=True, exist_ok=True)
            return os.getcwd() + '/exports'
        except Exception as e:
            raise Exception("Failed to create exports directory")

    def format_filename(self, filename: str) -> str:
        return self.export_path + '/' + filename
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return "Seeder()"
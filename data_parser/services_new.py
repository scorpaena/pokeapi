import requests
from datetime import datetime
import csv
import sys


class GetJSONDataFromAPI:
    
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        return response.json()
    
    def get_character_name(self):
        return self.url.split('/')[-1]


class TransformJSONtoCSV:
    
    def __init__(self):
        self.now = datetime.now().strftime('%m-%d-%y %H:%M:%S')

    def create_csv_file_name(self, character_name):
        return f'{character_name}_{self.now}.csv'

    def create_csv_file(self, json_data, file_name):
        with open(f'data_parser/csv_files/{file_name}', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerow(json_data.keys())
            csv_writer.writerow(json_data.values())


class TransformCSVtoJSON:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.json_data = {}

    def get_csv_file(self):
        return f'data_parser/csv_files/{self.file_name}'

    def create_json_view(self):
        csv.field_size_limit(sys.maxsize)
        file = self.get_csv_file()
        with open(file, newline = '') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.json_data.update(row)
        return self.json_data

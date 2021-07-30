import requests
import petl as etl
from datetime import datetime
import glob
import os
import pandas as pd
import csv
import json

# list_of_files = glob.glob(
#     '/home/linuxlite/Documents/django3.2/pokeapi/data_parser/csv_files/*.csv'
# )
# latest_file = max(list_of_files, key=os.path.getmtime)

# NOW = datetime.now().strftime('%m-%d-%y %H:%M:%S')

# URL = 'https://pokeapi.co/api/v2/pokemon/ditto'

class GetJSONDataFromAPI:
    
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        return response.json()


class TransformJSONtoCSV:
    
    def __init__(self):
        self.new_list = []
        self.names = []
        self.now = datetime.now().strftime('%m-%d-%y %H:%M:%S')

    def parse_nested_json(self, json_data, prefix=''):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                new_prefix = "{}.{}".format(prefix, key)
                self.parse_nested_json(json_data=value, prefix=new_prefix)
        elif isinstance(json_data, list):
            for index, value in enumerate(json_data):
                new_prefix = "{}{}".format(prefix, index)
                self.parse_nested_json(json_data=value, prefix=new_prefix)
        else:
            self.new_list.append(["{}".format(prefix), json_data])
        return self.new_list


    def transform_to_dataframe(self, parsed_json):
        df = pd.DataFrame.from_dict(parsed_json, orient='columns').T
        df.columns=df.iloc[0]
        for i in df.columns:
            self.names.append(i.split('.')[1])
        df.columns=self.names
        df = df.drop(index=0)
        return df


    def make_csv_file_name(self, url):
        name = url.split('/')[-1]
        return f'{name}_{self.now}.csv'


    def create_csv_file(self, data, file_name):
        return data.to_csv(f'data_parser/csv_files/{file_name}', index=False)


class TransformCSVtoJSON:
    
    def __init__(self, file):
        self.file = file
        self.json_array = []

    def create_json_view(self):
        with open(self.file, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.json_array.append(row)
        return self.json_array

# json = TransformCSVtoJSON(file='data_parser/csv_files/charmander_07-30-21 12:50:26.csv')
# print(json.create_json_view())
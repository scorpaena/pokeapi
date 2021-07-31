import requests
# import petl as etl
from datetime import datetime
# import glob
import os
# import pandas as pd
import csv
# import json


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

    def create_csv_file_name(self, url):
        name = url.split('/')[-1]
        return f'{name}_{self.now}.csv'

    def create_csv_file(self, json_data, file_name):
        with open(f'data_parser/csv_files/{file_name}', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            # csv_writer.writerow(json_data.keys())
            # for data in json_data:
            csv_writer.writerow(json_data.keys())
            csv_writer.writerow(json_data.values())

    # def create_csv_file(self, json_data, file_name):
    #     with open(f'data_parser/csv_files/{file_name}', 'w') as csv_file:
    #         csv_writer = csv.writer(csv_file, lineterminator='\n')
    #         csv_writer.writerow(json_data.keys())
    #         for data in json_data:
    #             csv_writer.writerow(json_data.values())
'''
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
'''

class TransformCSVtoJSON:
    
    def __init__(self):
        # self.file = file
        self.json_array = []

    def get_csv_file(self, file_name):
        return f'data_parser/csv_files/{file_name}'

    def create_json_view(self, file):
        # file = self.get_csv_file(file_name)
        with open(file, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.json_array.append(row)
        return self.json_array


# def get_file(file_name):
#     return f'data_parser/csv_files/{file_name}'
    # path = f'data_parser/csv_files/{file_name}'
    # for files in os.walk(path):
    #     file = files.find(file_name)
    #         if found != -1:
    #             print()
    #             print(fileName, 'Found\n')
    #             break
    #     except:
    #         exit()

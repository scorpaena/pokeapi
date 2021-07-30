import requests
import petl as etl
from datetime import datetime
import glob
import os
import pandas as pd

list_of_files = glob.glob(
    '/home/linuxlite/Documents/django3.2/pokeapi/data_parser/csv_files/*.csv'
)
latest_file = max(list_of_files, key=os.path.getmtime)

NOW = datetime.now().strftime('%m-%d-%y %H:%M:%S')

URL = 'https://pokeapi.co/api/v2/pokemon/ditto'


def get_json_data_from_url(url=URL):
    response = requests.get(url)
    json_data = response.json()
    return json_data


new_list=[]
def parse_nested_json(json_data, prefix=''):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            new_key = "{}.{}".format(prefix, key)
            parse_nested_json(value, new_key)
    elif isinstance(json_data, list):
        for index, value in enumerate(json_data):
            new_key = "{}{}".format(prefix, index)
            parse_nested_json(value, new_key)
    else:
        new_list.append(["{}".format(prefix), json_data])
    return new_list


def transform_to_dataframe(data):
    df = pd.DataFrame.from_dict(data, orient='columns').T
    df.columns=df.iloc[0]
    names=[]
    for i in df.columns:
        names.append(i.split('.')[1])
    df.columns=names
    df = df.drop(index=0)
    return df


def create_csv_file(data):
    return data.to_csv(f'csv_files/poke_{NOW}.csv', index=False)


def table_from_csv():
    table = etl.fromcsv(f'{latest_file}')
    return table


def list_result_csv_file():
    json_data = get_json_data_from_url()
    new_list = parse_nested_json(json_data=json_data)
    data = transform_to_dataframe(data=new_list)
    file = create_csv_file(data=data)
    table_from_csv()

list_result_csv_file()
import requests
import csv
import json
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

# def create_csv_file(json_data):
#     with open(f'csv_files/poke_{NOW}.csv', 'w') as csv_file:
#         csv_writer = csv.writer(csv_file, lineterminator='\n')#, quoting=csv.QUOTE_ALL)
#         # for data in json_data:
#         csv_writer.writerow(json_data.keys())


# def flatten_json(y):
#     out = {}

#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(y)
#     return out

g=[]
def print_dict(v, prefix=''):
    if isinstance(v, dict):
        for k, v2 in v.items():
            p2="{}.{}".format(prefix, k)
            print_dict(v2, p2)
    elif isinstance(v, list):
        for i, v2 in enumerate(v):
            p2="{}{}".format(prefix, i)
            print_dict(v2, p2)
    else:
        g.append(["{}".format(prefix), v])
    return g

df = pd.DataFrame.from_dict(print_dict(get_json_data_from_url()), orient='columns').T
df.columns=df.iloc[0]
# df.drop(df.index[1])

# print(df)

names_=[]
for i in df.columns:
    names_.append(i.split('.')[1])
names_

df.columns=names_
# df.drop(df.index[0])
df = df.drop(index=0)
# print(df)
# df = df.to_csv(f'csv_files/poke_{NOW}.csv', index=False)

# print(df)
# def get_names(list):
#     for i in list.c

# print(flatten_json(get_json_data_from_url()))
# print(print_dict(get_json_data_from_url()))


# def create_csv_file(json_data):
#     with open(f'csv_files/poke_{NOW}.csv', 'w') as csv_file:
#         csv_writer = csv.writer(csv_file, lineterminator='\n')#, quoting=csv.QUOTE_ALL)
#         count = 0
#         for data in json_data:
#             if count == 0:
#                 csv_writer.writerow(json_data.keys())
#                 count += 1
#             csv_writer.writerow(json_data.values())

# def create_csv_file(json_data):
#     with open(f'csv_files/poke_{NOW}.csv', 'w') as csv_file:
#         csv_writer = csv.writer(csv_file, lineterminator='\n')#, quoting=csv.QUOTE_ALL)
#         header = json_data.keys()
#         csv_writer.writerow(header)
#         for data in json_data:
#             csv_writer.writerow(json_data.values())

def table_from_csv():
    table = etl.fromcsv('data_parser/csv_files/ditto_07-31-21 18:56:45.csv')
    return table.look()

# print(table_from_csv())
# create_csv_file(json_data=flatten_json(get_json_data_from_url()))
# print(get_json_data_from_url().keys())
# print(create_csv_file(json_data=get_json_data_from_url()))
# print((get_json_data_from_url().keys()))

def create_csv_file(json_data):
    with open(f'csv_files/poke_{NOW}.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, lineterminator='\n')#, quoting=csv.QUOTE_ALL)
        key_list = list(json_data.keys())
        for i in range(len(key_list)):
            for data in json_data[key_list[i]]:
                print(data)
        # csv_writer.writerow(header)
        # for data in json_data:
        #     csv_writer.writerow(json_data.values())
# print(create_csv_file(json_data=get_json_data_from_url()))

print(table_from_csv())
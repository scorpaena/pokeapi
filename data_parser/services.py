import requests
from datetime import datetime
import csv
from math import ceil


class APIClient:
    def __init__(self):
        self.people_url = "https://swapi.dev/api/people/"
        self.planets_url = "https://swapi.dev/api/planets/" 
        self.films_url = "https://swapi.dev/api/films/" 
        self.species_url = "https://swapi.dev/api/species/" 
        self.vehicles_url = "https://swapi.dev/api/vehicles/" 
        self.starships_url = "https://swapi.dev/api/starships/"

########
    def get_people_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.people_url + f'{id}'
            response = requests.get(page_url).json()['name']
        elif id is None and url is not None:
            response = requests.get(url).json()['name']
        else:
            response = []
        return response

    def get_planets_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.planets_url + f'{id}'
            response = requests.get(page_url).json()['name']
        elif id is None and url is not None:
            response = requests.get(url).json()['name']
        else:
            response = []
        return response

    def get_films_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.films_url + f'{id}'
            response = requests.get(page_url).json()['title']
        elif id is None and url is not None:
            response = requests.get(url).json()['title']
        else:
            response = []
        return response

    def get_species_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.species_url + f'{id}'
            response = requests.get(page_url).json()['name']
        elif id is None and url is not None:
            response = requests.get(url).json()['name']
        else:
            response = []
        return response

    def get_vehicles_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.vehicles_url + f'{id}'
            response = requests.get(page_url).json()['name']
        elif id is None and url is not None:
            response = requests.get(url).json()['name']
        else:
            response = []
        return response

    def get_starships_detail(self, id=None, url=None):
        if id is not None and url is None:
            page_url = self.starships_url + f'{id}'
            response = requests.get(page_url).json()['name']
        elif id is None and url is not None:
            response = requests.get(url).json()['name']
        else:
            response = []
        return response
########

    def get_people_per_page(self, page_number):
        page_url = self.people_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response

    def get_planets_per_page(self, page_number):
        page_url = self.planets_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response

    def get_films_per_page(self, page_number):
        page_url = self.films_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response

    def get_species_per_page(self, page_number):
        page_url = self.species_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response

    def get_vehicles_per_page(self, page_number):
        page_url = self.vehicles_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response

    def get_starships_per_page(self, page_number):
        page_url = self.starships_url + f'?page={page_number}'
        response = requests.get(page_url).json()
        return response
########

    def get_people_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_people_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list

    def get_planets_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_planets_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list

    def get_films_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_films_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list

    def get_species_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_species_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list

    def get_vehicles_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_vehicles_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list

    def get_starships_all(self):
        result_list = []
        page_number = 1
        next_page = True 
        while next_page is not None:
            response = self.get_starships_per_page(page_number)
            page_number += 1
            next_page = response['next']
            for item in response['results']:
                result_list.append(item)
        return result_list
########


class APIDataProcessor:
    def __init__(self):
        self.api_client = APIClient()

    def people_per_page_data_set(self):
        raw_data = self.api_client.get_people_per_page(page_number=2)
        data = raw_data['results']
        data_set = []
        for item in data:
            result_dict = {}
            for key in item:
                if key == 'homeworld':
                    result_dict[key] = self.api_client.get_planets_detail(url=item[key])
                elif key == 'films':
                    result_dict[key] = [
                    self.api_client.get_films_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'species':
                    result_dict[key] = [
                    self.api_client.get_species_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'vehicles':
                    result_dict[key] = [
                    self.api_client.get_vehicles_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'starships':
                    result_dict[key] = [
                    self.api_client.get_starships_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                else:
                    result_dict[key] = item[key]
            data_set.append(result_dict)
            yield data_set


    def people_all_data_set(self):
        data = self.api_client.get_people_all()
        # data_set = []
        for item in data:
            result_dict = {}
            for key in item:
                if key == 'homeworld':
                    result_dict[key] = self.api_client.get_planets_detail(url=item[key])
                elif key == 'films':
                    result_dict[key] = [
                    self.api_client.get_films_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'species':
                    result_dict[key] = [
                    self.api_client.get_species_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'vehicles':
                    result_dict[key] = [
                    self.api_client.get_vehicles_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                elif key == 'starships':
                    result_dict[key] = [
                    self.api_client.get_starships_detail(url=item[key][i]) for i in range(len(item[key]))
                    ]
                else:
                    result_dict[key] = item[key]
            # data_set.append(result_dict)
            # yield data_set
            yield result_dict






# a = APIClient()
# data = a.get_people_all()
# print(data)


# a = APIDataProcessor()
# b = a.people_all_data_set()
# # b = a.people_per_page_data_set()
# # c = list(b)
# for i in range(3):
#     print(next(b))
# print(c)
# print(b)

# b = a.people_all_data_set()
# c = list(b)
# print(c)
# print(b)
# for i in range(2):
#     print(next(b))


class TransformJSONtoCSV:
    def __init__(self):
        self.data_processor = APIDataProcessor()

    def create_csv_file(self, file_name):
        data_to_save = self.data_processor.people_all_data_set()
        with open(f"data_parser/csv_files/{file_name}", "w") as csv_file:
            # csv_writer = csv.writer(csv_file, lineterminator="\n")
            csv_columns = ['name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','homeworld','films','species','vehicles','starships','created','edited','url']
            csv_writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            csv_writer.writeheader()
            for item in data_to_save:
                # csv_writer.writeheader()
                csv_writer.writerow(item)
                # csv_writer.writerow([key, value])


def csv_file_name():
    now = datetime.now().strftime("%m-%d-%y %H:%M:%S")
    return f"people_{now}.csv"


file_name = csv_file_name()
p = TransformJSONtoCSV()
p.create_csv_file(file_name)
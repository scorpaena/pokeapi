import requests
from datetime import datetime
import csv


class APIClient:
    def __init__(self):
        self.people_url = "https://swapi.dev/api/people/"
        self.planets_url = "https://swapi.dev/api/planets/"
        self.films_url = "https://swapi.dev/api/films/"
        self.species_url = "https://swapi.dev/api/species/"
        self.vehicles_url = "https://swapi.dev/api/vehicles/"
        self.starships_url = "https://swapi.dev/api/starships/"

    def get_people_detail(self, url):
        response = requests.get(url).json()["name"]
        return response

    def get_planets_detail(self, url):
        response = requests.get(url).json()["name"]
        return response

    def get_films_detail(self, url):
        response = requests.get(url).json()["title"]
        return response

    def get_species_detail(self, url):
        response = requests.get(url).json()["name"]
        return response

    def get_vehicles_detail(self, url):
        response = requests.get(url).json()["name"]
        return response

    def get_starships_detail(self, url):
        response = requests.get(url).json()["name"]
        return response

    def get_people_per_page(self, page_number):
        page_url = self.people_url + f"?page={page_number}"
        response = requests.get(page_url).json()
        return response

    def get_people_all(self):
        result_list = []
        page_number = 1
        next_page = True
        while next_page is not None:
            response = self.get_people_per_page(page_number)
            page_number += 1
            next_page = response["next"]
            for item in response["results"]:
                result_list.append(item)
        return result_list


class APIDataProcessor:
    def __init__(self):
        self.api_client = APIClient()

    def people_all_data_set(self):
        data = self.api_client.get_people_all()
        for item in data:
            result_dict = {}
            for key in item:
                if key == "homeworld":
                    result_dict[key] = self.api_client.get_planets_detail(url=item[key])
                elif key == "films":
                    result_dict[key] = [
                        self.api_client.get_films_detail(url=item[key][i])
                        for i in range(len(item[key]))
                    ]
                elif key == "species":
                    result_dict[key] = [
                        self.api_client.get_species_detail(url=item[key][i])
                        for i in range(len(item[key]))
                    ]
                elif key == "vehicles":
                    result_dict[key] = [
                        self.api_client.get_vehicles_detail(url=item[key][i])
                        for i in range(len(item[key]))
                    ]
                elif key == "starships":
                    result_dict[key] = [
                        self.api_client.get_starships_detail(url=item[key][i])
                        for i in range(len(item[key]))
                    ]
                else:
                    result_dict[key] = item[key]
            yield result_dict


class TransformJSONtoCSV:
    def __init__(self):
        self.data_processor = APIDataProcessor()
        self.csv_columns = [
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",
            "films",
            "species",
            "vehicles",
            "starships",
            "created",
            "edited",
            "url",
        ]

    def create_csv_file(self, file_name):
        data_to_save = self.data_processor.people_all_data_set()
        with open(f"data_parser/csv_files/{file_name}", "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.csv_columns)
            csv_writer.writeheader()
            for item in data_to_save:
                csv_writer.writerow(item)


def csv_file_name():
    now = datetime.now().strftime("%m-%d-%y %H:%M:%S")
    return f"people_{now}.csv"

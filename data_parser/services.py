import requests
from datetime import datetime
import csv
import re
from urllib.parse import urljoin
from django.core.exceptions import ObjectDoesNotExist


class APIClient:
    def __init__(self):
        self.base_url = "https://swapi.py4e.com/api/"

    def _item_url_parser(self, url):
        match = re.search(r"\d+/$", url) or re.search(r"\d+$", url)
        if match is None:
            raise ValueError(f"{url} doesn't contain item ID")
        id = url[match.start() : match.end()]
        return id

    def _resource_url_generator(self, resource):
        return urljoin(self.base_url, resource)

    def _item_url_generator(self, resource, url):
        resource_path = self._resource_url_generator(resource)
        id = self._item_url_parser(url)
        return urljoin(resource_path, id)

    def _get_object_from_url(self, resource, url):
        path = self._item_url_generator(resource, url)
        response = requests.get(url)
        if response.status_code != 200:
            raise ObjectDoesNotExist(f'{url} has no data')
        return response.json()

    def _get_lookup_value(self, resource, lookup_key, url):
        try:
            value = self._get_object_from_url(resource, url)[lookup_key]
        except KeyError:
            print(f"{url} item does not have {lookup_key} attribute")
        return value

    def _get_lookup_values_list(self, resource, lookup_key, url_list):
        values_list = []
        for url in url_list:
            values_list.append(self._get_lookup_value(resource, lookup_key, url))
        return values_list

    def _get_data_per_page(self, page_number, resource):
        page_url = self._resource_url_generator(resource)
        return requests.get(page_url, params={"page": page_number}).json()

    def _get_data_all(self, resource):
        result_list = []
        page_number = 1
        next_page = True
        while next_page is not None:
            response = self._get_data_per_page(page_number, resource)
            page_number += 1
            next_page = response["next"]
            for item in response["results"]:
                result_list.append(item)
        return result_list

    def get_planets_detail(self, url, resource="planets/", lookup_key="name"):
        return self._get_lookup_value(resource, lookup_key, url)

    def get_films_detail(self, url_list, resource="films/", lookup_key="title"):
        return self._get_lookup_values_list(resource, lookup_key, url_list)

    def get_species_detail(self, url_list, resource="species/", lookup_key="name"):
        return self._get_lookup_values_list(resource, lookup_key, url_list)

    def get_vehicles_detail(self, url_list, resource="vehicles/", lookup_key="name"):
        return self._get_lookup_values_list(resource, lookup_key, url_list)

    def get_starships_detail(self, url_list, resource="starships/", lookup_key="name"):
        return self._get_lookup_values_list(resource, lookup_key, url_list)

    def get_people_per_page(self, page_number, resource="people/"):
        return self._get_data_per_page(page_number, resource)

    def get_people_all(self, resource="people/"):
        return self._get_data_all(resource)


class APIDataProcessor:
    def __init__(self):
        self.api_client = APIClient()

    def people_all_data_set(self):
        data = self.api_client.get_people_all()
        for item in data:
            result_dict = {}
            for key in item:
                result_dict[key] = item[key]
                result_dict["homeworld"] = self.api_client.get_planets_detail(
                    url=item["homeworld"]
                )
                result_dict["films"] = self.api_client.get_films_detail(
                    url_list=item["films"]
                )
                result_dict["species"] = self.api_client.get_species_detail(
                    url_list=item["species"]
                )
                result_dict["vehicles"] = self.api_client.get_vehicles_detail(
                    url_list=item["vehicles"]
                )
                result_dict["starships"] = self.api_client.get_starships_detail(
                    url_list=item["starships"]
                )
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

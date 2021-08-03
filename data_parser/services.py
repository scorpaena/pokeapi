import requests
from datetime import datetime
import csv
from math import ceil


class GetPaginationParameter:
    def __init__(self):
        self.people_url = "https://swapi.dev/api/people/"

    def get_people_count(self):
        response = requests.get(self.people_url).json()
        return response.get("count")

    def get_pages_count(self):
        count = self.get_people_count()
        return ceil(count / 10)


class GetPeopleFromAPI:
    def __init__(self):
        self.people_url = "https://swapi.dev/api/people/"
        self.lookup_dict = {
            "homeworld": "name",
            "films": "title",
            "species": "name",
            "vehicles": "name",
            "starships": "name",
        }

    def get_people_url(self, pages_count):
        url_list = []
        for i in range(1, pages_count + 1):
            url = self.people_url + f"?page={i}"
            url_list.append(url)
        return url_list

    def get_item_name_from_url(self, lookup_key, urls):
        items_list = []
        lookup_value = self.lookup_dict[lookup_key]
        if isinstance(urls, list) and len(urls) > 1:
            for url in urls:
                response = requests.get(url).json()
                item = response.get(lookup_value)
                items_list.append(item)
            return items_list
        elif isinstance(urls, list) and len(urls) == 0:
            return []
        elif isinstance(urls, list) and len(urls) == 1:
            response = requests.get(urls[0]).json()
            return response.get(lookup_value)
        else:
            response = requests.get(urls).json()
            return response.get(lookup_value)

    def get_people(self, pages_count):
        result_dict = {}
        url_list = self.get_people_url(pages_count)
        for url in url_list:
            response = requests.get(url).json()
            for item in response["results"]:
                for key in item:
                    if key in self.lookup_dict.keys():
                        result_dict[key] = self.get_item_name_from_url(
                            lookup_key=key, urls=item[key]
                        )
                    else:
                        result_dict[key] = item[key]
                yield result_dict


class TransformJSONtoCSV:
    def create_csv_file(self, file_name, people, people_count):
        with open(f"data_parser/csv_files/{file_name}", "w") as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator="\n")
            for i in range(people_count):
                csv_writer.writerow(people)


def csv_file_name():
    now = datetime.now().strftime("%m-%d-%y %H:%M:%S")
    return f"people_{now}.csv"

import pytest
import os
from pathlib import Path
from data_parser.services import (
    APIClient,
    APIDataProcessor,
    TransformJSONtoCSV,
    csv_file_name,
)


@pytest.fixture
def csv():
    return TransformJSONtoCSV()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def file_name():
    return csv_file_name()


def test_csv_file_name():
    file_name = csv_file_name()
    assert file_name.startswith("people") == True


def test_item_url_parser(api_client):
    id = api_client._item_url_parser(url="https://swapi.dev/api/people/1/")
    assert id == "1/"


def test_item_url_parser1(api_client):
    id = api_client._item_url_parser(url="https://swapi.dev/api/people/1")
    assert id == "1"


def test_resource_url_generator(api_client):
    path = api_client._resource_url_generator(resource="people/")
    assert path == "https://gorest.co.in/people/"


def test_item_url_generator(api_client):
    path = api_client._item_url_generator(
        resource="people/", url="https://gorest.co.in/people/1/"
    )
    assert path == "https://gorest.co.in/people/1/"


"""
def test_api_client_planets(api_client):
    planets = api_client.get_planets_detail(url="https://swapi.dev/api/planets/1/")
    assert planets == "Tatooine"


def test_api_client_films(api_client):
    films = api_client.get_films_detail(url="https://swapi.dev/api/films/1/")
    assert films == "A New Hope"


def test_api_client_species(api_client):
    species = api_client.get_species_detail(url="https://swapi.dev/api/species/1/")
    assert species == "Human"


def test_api_client_vehicles(api_client):
    vehicles = api_client.get_vehicles_detail(url="https://swapi.dev/api/vehicles/4/")
    assert vehicles == "Sand Crawler"


def test_api_client_starships(api_client):
    starships = api_client.get_starships_detail(
        url="https://swapi.dev/api/starships/2/"
    )
    assert starships == "CR90 corvette"


def test_transform_to_csv(csv, file_name):
    csv.create_csv_file(file_name)
    file = Path(f"data_parser/csv_files/{file_name}")
    file_not_empty = os.stat(file).st_size
    assert file.is_file() == True
    assert file_not_empty != 0
"""

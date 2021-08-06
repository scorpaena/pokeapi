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

@pytest.fixture
def url():
    return 'https://swapi.py4e.com/api/planets/1/'

@pytest.fixture
def url1():
    return 'https://swapi.py4e.com/api/planets/1'

@pytest.fixture
def url_list():
    return [
    'https://swapi.py4e.com/api/planets/1',
    'https://swapi.py4e.com/api/planets/2/',
    'https://swapi.py4e.com/api/planets/3'
    ]

@pytest.fixture
def resource():
    return 'planets/'

@pytest.fixture
def lookup_key():
    return "name"

@pytest.fixture
def resource1():
    return 'people/'


def test_csv_file_name():
    file_name = csv_file_name()
    assert file_name.startswith("people") == True


def test_item_url_parser(api_client, url):
    id = api_client._item_url_parser(url)
    assert id == "1/"


def test_item_url_parser1(api_client, url1):
    id = api_client._item_url_parser(url1)
    assert id == "1"


def test_resource_url_generator(api_client, resource):
    path = api_client._resource_url_generator(resource)
    assert path == "https://swapi.py4e.com/api/planets/"


def test_item_url_generator(api_client, resource, url):
    path = api_client._item_url_generator(resource, url)
    assert path == 'https://swapi.py4e.com/api/planets/1/'


def test_get_object_from_url(api_client, resource, url, lookup_key):
    response = api_client._get_object_from_url(resource, url)
    assert response[lookup_key] != None


def test_get_lookup_value(api_client, resource, lookup_key, url):
    value = api_client._get_lookup_value(resource, lookup_key, url)
    assert isinstance(value, str) == True
    assert len(value) != 0


def test_get_lookup_values_list(api_client, resource, lookup_key, url_list):
    value = api_client._get_lookup_values_list(resource, lookup_key, url_list)
    assert isinstance(value, list) == True
    assert len(value) == 3


def test_get_data_per_page(api_client, resource1):
    data = api_client._get_data_per_page(resource=resource1, page_number=1)
    assert data['results'][0]['name'] == 'Luke Skywalker'


def test_transform_to_csv(csv, file_name):
    csv.create_csv_file(file_name)
    file = Path(f"data_parser/csv_files/{file_name}")
    file_not_empty = os.stat(file).st_size
    assert file.is_file() == True
    assert file_not_empty != 0

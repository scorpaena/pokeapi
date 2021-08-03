import pytest
from pathlib import Path
from data_parser.services import (
    TransformJSONtoCSV,
    GetPaginationParameter,
    GetPeopleFromAPI,
    csv_file_name,
)


@pytest.fixture
def url():
    return "https://swapi.dev/api/people/"


@pytest.fixture
def pages_count():
    parameter = GetPaginationParameter()
    return parameter.get_pages_count()


@pytest.fixture
def people_count():
    parameter = GetPaginationParameter()
    return parameter.get_people_count()


@pytest.fixture
def people(pages_count):
    people_blank = GetPeopleFromAPI()
    return people_blank.get_people(pages_count)


@pytest.fixture
def file_name():
    return csv_file_name()


def test_csv_file_name():
    file_name = csv_file_name()
    assert file_name.startswith("people") == True


def test_data():
    people_blank = GetPeopleFromAPI()
    people = people_blank.get_people(pages_count=1)
    assert str(type(people)) == "<class 'generator'>"


def test_transform_to_csv(people, file_name, people_count):
    blank = TransformJSONtoCSV()
    file = blank.create_csv_file(file_name, people, people_count)
    my_file = Path(f"data_parser/csv_files/{file_name}")
    assert my_file.is_file() == True

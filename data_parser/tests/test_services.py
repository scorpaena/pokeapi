import pytest
from pathlib import Path
from data_parser.services import (
    TransformJSONtoCSV, 
    GetPaginationParameter, 
    GetPeopleFromAPI,
    csv_file_name
)

@pytest.fixture
def url():
    return 'https://swapi.dev/api/people/'

def test_csv_file_name():
    file_name = csv_file_name()
    assert file_name.startswith('people') == True

def test_data():
    people_blank = GetPeopleFromAPI()
    people = people_blank.get_people(pages_count=1)
    assert str(type(people)) == "<class 'generator'>"

def test_transform_to_csv():
    parameter = GetPaginationParameter()
    people_count = parameter.get_people_count()
    pages_count = parameter.get_pages_count()
    people_blank = GetPeopleFromAPI()
    people = people_blank.get_people(pages_count=pages_count)
    file_name = csv_file_name()
    blank = TransformJSONtoCSV()
    file = blank.create_csv_file(file_name=file_name, people=people, people_count=people_count)
    # my_file = Path(f"data_parser/csv_files/{file_name}")
    # assert my_file.is_file() == True

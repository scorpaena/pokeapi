import pytest
from pathlib import Path
from data_parser.services import (
    GetName, 
    GetJSONDataFromAPI, 
    TransformJSONtoCSV, 
    TransformCSVtoJSON
)

@pytest.fixture
def url():
    return 'https://pokeapi.co/api/v2/pokemon/beedrill'

def test_get_name(url):
    name = GetName(url)
    character_name = name.get_character_name()
    file_name = name.get_csv_file_name(character_name)
    assert character_name == 'beedrill'
    assert file_name.startswith('beedrill') == True

def test_data(url):
    data = GetJSONDataFromAPI(url)
    json_data = data.get_data()
    assert str(type(json_data)) == "<class 'dict'>"

def test_transform_to_csv(url):
    name = GetName(url)
    character_name = name.get_character_name()
    file_name = name.get_csv_file_name(character_name)
    data = GetJSONDataFromAPI(url)
    json_data = data.get_data()
    blank = TransformJSONtoCSV()
    file = blank.create_csv_file(json_data, file_name)
    my_file = Path(f"data_parser/csv_files/{file_name}")
    assert my_file.is_file() == True

def test_transform_to_json(url):
    name = GetName(url)
    character_name = name.get_character_name()
    file_name = name.get_csv_file_name(character_name)
    data = GetJSONDataFromAPI(url)
    json_data = data.get_data()
    blank = TransformJSONtoCSV()
    file = blank.create_csv_file(json_data, file_name)
    json_blank = TransformCSVtoJSON(file_name)
    json_data = json_blank.create_json_view()
    assert str(type(json_data)) == "<class 'dict'>"

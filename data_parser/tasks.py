from pokeapi.celery import app
from .services import (
    GetPaginationParameter, 
    GetPeopleFromAPI, 
    TransformJSONtoCSV
)

@app.task
def download_data_from_api(file_name):
    parameter = GetPaginationParameter()
    people_count = parameter.get_people_count()
    pages_count = parameter.get_pages_count()

    people_blank = GetPeopleFromAPI()
    people = people_blank.get_people(pages_count)

    csv = TransformJSONtoCSV()
    csv.create_csv_file(file_name, people, people_count)

from pokeapi.celery import app
from .services import TransformJSONtoCSV


@app.task
def download_data_from_api(file_name):
    csv = TransformJSONtoCSV()
    csv.create_csv_file(file_name)

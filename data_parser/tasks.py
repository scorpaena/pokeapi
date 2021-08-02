from pokeapi.celery import app
from .services import GetJSONDataFromAPI, TransformJSONtoCSV, send_email

@app.task
def download_data_from_api(url, file_name):
    data_from_api = GetJSONDataFromAPI(url)
    json_data = data_from_api.get_data()
    csv = TransformJSONtoCSV()
    csv.create_csv_file(json_data, file_name)
    send_email(file_name)
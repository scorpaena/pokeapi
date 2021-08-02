from pokeapi.celery import app
from data_parser.tasks import download_data_from_api
import pytest


@pytest.fixture
def celery_app(request):
    app.conf.update(CELERY_ALWAYS_EAGER=True)
    return app

def test_task(celery_app):
    url = 'https://pokeapi.co/api/v2/pokemon/beedrill'
    file_name = 'beedrill'
    download_data_from_api.delay(url, file_name)

from django.urls import path
from .views import PokeFileDownLoadView, PokeCSVFileView

urlpatterns = [
    path("load_file", PokeFileDownLoadView.as_view()),
    path("files", PokeCSVFileView.as_view()),
]
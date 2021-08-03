from django.urls import path
from .views import PokeFileDownLoadView, PokeCSVFileView

urlpatterns = [
    path("files/", PokeFileDownLoadView.as_view()),
    path("files/<pk>", PokeCSVFileView.as_view()),
]

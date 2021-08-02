from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .serializers import PokeFilesSerializer, PokeFileDetailSerializer
from .models import PokeFilesModel
from .services import TransformCSVtoJSON, GetName
from .filters import PokeFilesModelFilter
from .tasks import download_data_from_api


class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFilesSerializer
    filterset_class = PokeFilesModelFilter

    def perform_create(self, serializer):
        url = self.request.data.get("url")
        name = GetName(url)
        character_name = name.get_character_name()
        file_name = name.get_csv_file_name(character_name)
        download_data_from_api.delay(url, file_name)
        serializer.save(
            url=url,
            character_name=character_name,
            file_name=file_name,
        )


class PokeCSVFileView(generics.RetrieveAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFileDetailSerializer

    def get_object(self):
        file_name = super().get_object().file_name
        object = TransformCSVtoJSON(file_name)
        return object.create_json_view()

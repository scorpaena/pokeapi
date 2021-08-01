from rest_framework import generics
from .serializers import PokeFilesSerializer, PokeFileDetailSerializer
from .models import PokeFilesModel
from .services_new import TransformCSVtoJSON
from .filters import PokeFilesModelFilter


class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFilesSerializer
    filterset_class = PokeFilesModelFilter


class PokeCSVFileView(generics.RetrieveAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFileDetailSerializer

    def get_object(self):
        file_name = super().get_object().file_name
        object = TransformCSVtoJSON(file_name)
        return object.create_json_view()

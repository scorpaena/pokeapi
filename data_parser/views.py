from rest_framework import generics
from .serializers import PokeFilesSerializer, PokeFileDetailSerializer
from .models import PokeFilesModel
from .filters import PokeFilesModelFilter


class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFilesSerializer
    filterset_class = PokeFilesModelFilter


class PokeCSVFileView(generics.RetrieveAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFileDetailSerializer

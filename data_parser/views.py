from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination
from .serializers import PokeFilesSerializer
from .models import PokeFilesModel
from .filters import PokeFilesModelFilter
from .services import CSVFileProcessor


class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFilesModel.objects.all()
    serializer_class = PokeFilesSerializer
    filterset_class = PokeFilesModelFilter


class PokeCSVFileView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        paginator = CursorPagination()
        csv = CSVFileProcessor()
        data = csv.read_from_csv_file(id)
        # response = paginator.get_paginated_response(data)
        return Response(data)

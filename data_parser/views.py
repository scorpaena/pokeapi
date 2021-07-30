from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_csv.renderers import CSVRenderer
from .serializers import PokeFileDownLoadSerializer
from .models import PokeFileDownLoadModel
from .services_new import TransformCSVtoJSON
# from .services import table_from_csv

class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFileDownLoadModel.objects.all()
    serializer_class = PokeFileDownLoadSerializer


class PokeCSVFileView(APIView):
    # renderer_classes = [CSVRenderer,]

    def get(self, request, format=None):
        json = TransformCSVtoJSON(file='data_parser/csv_files/ditto_07-30-21 14:43:23.csv')
        content = json.create_json_view()
        return Response(content)
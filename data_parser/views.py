from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_csv.renderers import CSVRenderer
from .serializers import PokeFileDownLoadSerializer
from .models import PokeFileDownLoadModel
from .services import table_from_csv

class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFileDownLoadModel.objects.all()
    serializer_class = PokeFileDownLoadSerializer


class PokeCSVFileView(APIView):
    renderer_classes = [CSVRenderer,]

    def get(self, request, format='text/csv'):
        # users = User.objects.filter(active=True)
        content = table_from_csv()
        return Response(content)
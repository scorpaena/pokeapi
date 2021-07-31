from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_csv.renderers import CSVRenderer
from .serializers import PokeFileDownLoadSerializer, PokeFileSerializer
from .models import PokeFileDownLoadModel
from .services_new import TransformCSVtoJSON
# from .services import table_from_csv

class PokeFileDownLoadView(generics.ListCreateAPIView):
    queryset = PokeFileDownLoadModel.objects.all()
    serializer_class = PokeFileDownLoadSerializer


class PokeCSVFileView(generics.RetrieveAPIView):
    queryset = PokeFileDownLoadModel.objects.all()
    serializer_class = PokeFileSerializer

    def get_object(self):
        file_name = super().get_object().file_name
        view = TransformCSVtoJSON()
        file = view.get_csv_file(file_name)
        return view.create_json_view(file)




    # def get(self, request, format=None):
    #     json = TransformCSVtoJSON(file='data_parser/csv_files/charmander_07-31-21 11:53:01.csv')
    #     content = json.create_json_view()
    #     return Response(content)

# class PokeCSVFileView(APIView):

#     def get(self, request, format=None):
#         json = TransformCSVtoJSON(file='data_parser/csv_files/charmander_07-31-21 11:53:01.csv')
#         content = json.create_json_view()
#         return Response(content)
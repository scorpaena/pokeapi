from rest_framework import serializers
from .models import PokeFilesModel
from .services import csv_file_name
from .tasks import download_data_from_api


class PokeFilesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        file_name = csv_file_name()
        validated_data["file_name"] = file_name
        download_data_from_api.delay(file_name)
        return super().create(validated_data)

    class Meta:
        model = PokeFilesModel
        fields = [
            "id",
            "file_name",
            "url",
            "date",
        ]
        read_only_fields = [
            "id",
            "file_name",
            "url",
            "date",
        ]


# class PokeFileDetailSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     height = serializers.CharField()
#     mass = serializers.CharField()
#     hair_color = serializers.CharField()
#     skin_color = serializers.CharField()
#     eye_color = serializers.CharField()
#     birth_year = serializers.CharField()
#     gender = serializers.CharField()
#     homeworld = serializers.CharField()
#     films = serializers.CharField()
#     species = serializers.CharField()
#     vehicles = serializers.CharField()
#     starships = serializers.CharField()
#     created = serializers.DateTimeField()
#     edited = serializers.DateTimeField()
#     url =serializers.URLField()

#     class Meta:
#         fields = [
#             'name',
#             'height',
#             'mass',
#             'hair_color',
#             'skin_color',
#             'eye_color',
#             'birth_year',
#             'gender',
#             'homeworld',
#             'films',
#             'species',
#             'vehicles',
#             'starships',
#             'created',
#             'edited',
#             'url',
#         ]
#         read_only_fields = [
#             'name',
#             'height',
#             'mass',
#             'hair_color',
#             'skin_color',
#             'eye_color',
#             'birth_year',
#             'gender',
#             'homeworld',
#             'films',
#             'species',
#             'vehicles',
#             'starships',
#             'created',
#             'edited',
#             'url',
#         ]

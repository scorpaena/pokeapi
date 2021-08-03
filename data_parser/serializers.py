from rest_framework import serializers
from .models import PokeFilesModel
from .services import csv_file_name
from .tasks import download_data_from_api


class PokeFilesSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        file_name = csv_file_name()
        validated_data['file_name'] = file_name
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


class PokeFileDetailSerializer(serializers.ModelSerializer):

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

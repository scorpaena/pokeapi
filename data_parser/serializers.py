from rest_framework import serializers
from .models import PokeFileDownLoadModel


class PokeFileDownLoadSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = PokeFileDownLoadModel
        fields = [
            "id",
            "file_name",
            "url",
            "date",
        ]
        read_only_fields = [
            "id",
            "file_name",
            "date",
        ]
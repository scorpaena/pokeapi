from rest_framework import serializers
from .models import PokeFilesModel


class PokeFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PokeFilesModel
        fields = [
            "id",
            "character_name",
            "file_name",
            "url",
            "date",
        ]
        read_only_fields = [
            "id",
            "character_name",
            "file_name",
            "date",
        ]


class PokeFileDetailSerializer(serializers.Serializer):

    abilities = serializers.JSONField()
    base_experience = serializers.IntegerField()
    forms = serializers.JSONField()
    game_indices = serializers.JSONField()
    height = serializers.IntegerField()
    held_items = serializers.JSONField()
    id = serializers.IntegerField()
    is_default = serializers.BooleanField()
    location_area_encounters = serializers.URLField()
    moves = serializers.JSONField()
    name = serializers.CharField(max_length=250)
    order = serializers.IntegerField()
    past_types = serializers.JSONField()
    species = serializers.JSONField()
    sprites = serializers.JSONField()
    stats = serializers.JSONField()
    types = serializers.JSONField()
    weight = serializers.IntegerField()

    class Meta:
        fields = [
            'abilities',
            'base_experience',
            'forms',
            'game_indices',
            'height',
            'held_items',
            'id',
            'is_default',
            'location_area_encounters',
            'moves',
            'name',
            'order',
            'past_types',
            'species',
            'sprites',
            'stats',
            'types',
            'weight',
        ]

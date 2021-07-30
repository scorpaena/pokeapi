from rest_framework import serializers
from .models import PokeFileDownLoadModel
from .services_new import GetJSONDataFromAPI, TransformJSONtoCSV


class PokeFileDownLoadSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        url = validated_data['url']
        json_data = GetJSONDataFromAPI(url).get_data()
        csv = TransformJSONtoCSV()
        parsed_json = csv.parse_nested_json(json_data)
        data = csv.transform_to_dataframe(parsed_json)
        file_name = csv.make_csv_file_name(url)
        csv.create_csv_file(data, file_name)
        return PokeFileDownLoadModel.objects.create(url=url, file_name=file_name)

   
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
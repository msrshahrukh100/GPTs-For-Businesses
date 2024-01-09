from rest_framework import serializers


class FileCreateSerializer(serializers.Serializer):
    file = serializers.FileField()


class FileSerializer(serializers.Serializer):      
    id = serializers.CharField()
    object = serializers.CharField()
    bytes = serializers.IntegerField()
    created_at = serializers.IntegerField()
    filename = serializers.CharField()
    purpose = serializers.CharField()

class FilesListSerializer(serializers.Serializer):
    data = FileSerializer(many=True)
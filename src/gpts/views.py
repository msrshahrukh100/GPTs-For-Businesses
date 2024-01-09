from rest_framework.response import Response
from .serializers import FileCreateSerializer, FilesListSerializer
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .utils import create_file, list_files

class FileCreate(generics.ListCreateAPIView):
    serializer_class = FileCreateSerializer
    parser_class = (MultiPartParser,)
    
    def create(self, request, *args, **kwargs):
        file_obj = request.FILES['file']       
        return Response(data=create_file(file_obj.file), status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        sd = FilesListSerializer(data=list_files())
        files_data = {}
        if sd.is_valid():
            files_data = sd.data
        print(sd.errors)
        return Response(data=files_data, status=status.HTTP_200_OK)


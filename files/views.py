from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import File
from .serializers import FileSerializer
from .tasks import process_uploaded_file


@api_view(['POST'])
def file_upload(request):
    serialized_obj = FileSerializer(data=request.data)
    if serialized_obj.is_valid():
        file_obj = serialized_obj.save()
        process_uploaded_file.delay(file_obj.id)
        return Response(serialized_obj.data, status=status.HTTP_201_CREATED)
    return Response(serialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def file_list(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

# from rest_framework import generics
# from .models import Library
# from .serializers import LibrarySerializer


# class ViewLibrarySet(generics.ListCreateAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibrarySerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from back.serializers import LibrarySerializer
from .models import Library    

class LibraryListAndCreate(APIView):
    def get(self, request):
        library = Library.objects.all()
        
        serializer = LibrarySerializer(library, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = LibrarySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

class LibraryEditAndDelete(APIView):

    def get_object(self, pk):
        try:
            return Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        library = self.get_object(pk)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)
    
    def put(self, request, pk):
        library = self.get_object(pk)
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        library = self.get_object(pk)
        library.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

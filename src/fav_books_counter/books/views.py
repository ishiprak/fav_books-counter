from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer 

# # Create your views here.
# class BookListView(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serialized_query = BookSerializer(queryset, many=True)
#         return Response(serialized_query.data)

class BookView(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

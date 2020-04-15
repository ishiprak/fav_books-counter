from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Book
from .serializers import BookSerializer, UserRegisterSerializer
from django.views.decorators.csrf import csrf_exempt

# # Create your views here.
# class BookListView(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serialized_query = BookSerializer(queryset, many=True)
#         return Response(serialized_query.data)

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['POST',])
@permission_classes([permissions.AllowAny])
def user_register_view(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            print("Yo man!!")
            data['response'] = 'Succesfully registered the user.'
            data['username'] = account.username
            data['email'] = account.email
            data['login'] = 'Request the url " http://localhost:8000/books/api/token " with request body of "username" and "password" for JWT token-pair generation.'
        else:
            data = serializer.errors
        return Response(data)



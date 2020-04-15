from rest_framework import serializers
from rest_framework.response import Response
from .models import Book
from django.contrib.auth import get_user_model, authenticate, login

user = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'genre',
            'amazon_url',
        )



class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # authentication_classes = [authentication.BasicAuthentication]
    class Meta:
        model = user
        fields = (
            'username',
            'email',
            'password',
            'password2',
        )
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self, *args, **kwargs):
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')
        if username and password:
            user_qs = user.objects.filter(username=username)
            email_qs = user.objects.filter(email=email)
            if user_qs.exists():
                raise serializers.ValidationError({"username" : "User with this username already exists, please provide another username."})
            if email_qs.exists():
                raise serializers.ValidationError({"email" : "This email is already registered, please provide another email."})
            if password != password2:
                raise serializers.ValidationError({
                                                    "password" : "Passwords do not match!",
                                                    "password1" : str(password),
                                                    "password2" : str(password2),
                                                    })
            user_account = user(username=self.validated_data.get('username'), email=self.validated_data.get('email'))
            user_account.set_password(password)
            user_account.save()
            return user_account
            

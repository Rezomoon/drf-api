
from django.contrib.auth import get_user_model 
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializers :

User = get_user_model()

class MyLoginSerializer(TokenObtainPairSerializer) :

    def validate(self, attrs):
        data = super().validate(attrs)

        data["is_staff"]            = self.user.is_staff
        data["is_authenticated"]    = self.user.is_authenticated
        data["is_admin"]            = self.user.is_admin  

        return data

class UserListSerializer(serializers.ModelSerializer) : 

    """
    Its Just For Users List
    """

    class Meta : 
        model   = User    
        fields  = "__all__"


class CreateUserSerializer(serializers.ModelSerializer) : 
    class Meta :
        model   = User
        fields  = ("email" , "password" )
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data ["email"],
            validated_data ["password"],)
        return user
class CreateAdminSerializer(serializers.ModelSerializer) : 

    class Meta :

        model   = User
        fields  = ("email" , "password")  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_admin(
            email = validated_data["email"] , 
            password = validated_data["password"]
        )
        return user
class CreateSuperUser(serializers.ModelSerializer):
    class Meta : 
        model   = User
        fields  = ("email" , "password") 
        extra_kwargs = {"password" :{"write_only" : True}}
    def create(self, validated_data):
        user = User.objects.create_superuser(
            email       = validated_data["email"] , 
            password    = validated_data["password"]
        )
        return user
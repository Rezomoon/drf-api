from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .queries.accounts_queries import UserListQueries
from .serializers.accounts_ser import UserListSerializer , MyLoginSerializer , CreateUserSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication , TokenAuthentication , BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions.back_per import IsAdminPermissions


# Create your views here.

class UserListViews(APIView) :
    permission_classes      = [IsAuthenticated ,IsAdminPermissions]

    def get(self ,request , format = None) : 

        queryset    = UserListQueries()

        serializer  = UserListSerializer(queryset , many = True)

        return Response(serializer.data)


from django.contrib.auth import user_logged_in
class Testing(APIView) : 
    # authentication_classes  = [BasicAuthentication]
    permission_classes      = [IsAuthenticated ]

    def get(self , request , format = None)  : # Format => Noe khoroji ro taeen mikone !
        content = {
            "method"    : request.method ,
            "path"      : request.path ,
            "get_full_path" : request.get_full_path() ,
            'META'      : str(request.META),
            "GET"       : request.GET ,
            "data"      : request.data ,
            "POST"      : request.POST ,
            'auth'      : str(request.auth),  # None
            "user"      : str(request.user.is_authenticated) , 
            "user_ip"   : request.META.get("REMOTE_ADDR")
              
        }
   
        return Response(data=content)




class CustomLogin(TokenObtainPairView):
    serializer_class = MyLoginSerializer


class AddUser(APIView) : 
    
    def post(self,request , format = None) :

        data        = request.data
        serializer  = CreateUserSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        user        = serializer.save()

        user        = UserListSerializer(user)
        
        return Response(user.data )
        

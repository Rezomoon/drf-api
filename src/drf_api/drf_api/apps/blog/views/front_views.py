from django.http import JsonResponse
from django.shortcuts import render
from drf_api.apps.blog.models import Blog
from drf_api.apps.blog.serializers.front_ser import BlogSerializer , BlogModelSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.



class BlogList(APIView) : 
    def get(self , request , format = None) :  # Format ????

        blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs , many = True)
        return Response(
            data= {
                'data' : serializer.data 
            }, 
            status=status.HTTP_200_OK
        )

    def post(self , request , format = None) : # Format ????

        data        = request.data 

        serializer  = BlogSerializer(data)

        if serializer.is_valid() :
            return Response (
                data= {
                    'data' : serializer.data
                } , 
                status=status.HTTP_201_CREATED
            )
        else : 
            return Response(

                data = {'errors' : serializer.errors } ,

                status=status.HTTP_406_NOT_ACCEPTABLE

                  )
         


class BlogDetails(APIView) : 
    def get_object(self , pk ) :

        try :

            blog = Blog.objects.get(id = pk)
            return blog

        except Blog.DoesNotExist : 

            return Response({"errors" : "blog does not exist"} , status=status.HTTP_400_BAD_REQUEST)
    def get(self , request , pk, format  = None) : 

        serializer = BlogSerializer(self.get_object(pk = pk) )
        return Response(data = {
            "data" : serializer.data
        } , 
        status=status.HTTP_200_OK
        )
    
    def put(self , request , pk , format  = None) : 

        data        = request.data
        serializer  = BlogSerializer(instance = self.get_object(pk) , data = data)
        if serializer.is_valid() :
            serializer.save()
            return Response(
                data = {
                    "data" : serializer.data , 

                } , 
                status=status.HTTP_200_OK
            )
    def delete(self, request , pk , format = None ) :
        blog = self.get_object(pk)
        blog.delete()
        return Response(
            data= {
                "data" : "Done"
            } , 
            status=status.HTTP_200_OK
        )


@csrf_exempt
@api_view(["GET" , "POST"]) # With this decorator we can access to request.data
def blog_view(request)  : 
    if request.method == "GET" : 

        blog_list   = Blog.objects.all()
        serializer  = BlogSerializer( blog_list, many = True).data
        return Response(
            {
            "data" : serializer
        } , status=status.HTTP_200_OK)
    
    elif request.method == "POST" :
        
        # data = JsonResponse().parse(request) # Baraye Ine k Data Daryafti ro parser konim

        data = request.data
        
        serializer = BlogSerializer(data)

        if serializer.is_valid() :

            serializer.save()
            return Response(
                data={
                    "data" : serializer.data
                } , 
                status=status.HTTP_201_CREATED
            )
        
        else : 

            return Response(
                data={
                    "data" : serializer.errors
                } , 
                status=status.HTTP_403_FORBIDDEN
            )



@api_view(["PUT"])
@csrf_exempt        
def blog_detail_view(request , blog_id) : 

    try : 
        blog = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist : 
        return Response({"errors" : "blog does not exist"} , status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET" : 

        serializer = BlogSerializer(blog)
        # return JsonResponse({
        #     "data" : serializer.data
        # })
        return Response (data  = {
            "data" : serializer.data
        } , 
        status=status.HTTP_200_OK)
    
    if request.method == "DELETE" : 

        blog.delete()
        return JsonResponse({
            "data" : "BLOG DELETED"
        })
    
    if request.method == "PUT" :

        # data = JSONParser().parse(request)
        data = request.data


        serializer = BlogSerializer(instance = blog , data = data)
        if serializer.is_valid() : 
            serializer.save()
            return JsonResponse({
                "data" : serializer.data
            })
        else : 
            return JsonResponse(
                {
                    "data" : serializer.errors
                }
            )
    
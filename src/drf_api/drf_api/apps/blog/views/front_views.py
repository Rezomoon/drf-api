from django.http import JsonResponse
from django.shortcuts import render
from drf_api.apps.blog.models import Blog
from drf_api.apps.blog.serializers.front_ser import BlogSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.


@csrf_exempt
@api_view(["GET" , "POST"]) # With this decorator we can access to request.data
def blog_view(request)  : 
    if request.method == "GET" : 

        blog_list = Blog.objects.all()
        serializer  = BlogSerializer( blog_list, many = True).data
        return Response(data={
            "data" : serializer.data
        } , status=status.HTTP_200_OK)
    
    elif request.method == "POST" :
        
        # data = JsonResponse().parse(request) # Baraye Ine k Data Daryafti ro parser konim

        data = request.data
        
        serializer = BlogSerializer(data)

        if serializer.is_valid() :

            serializer.save()
            return Response(
                {
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
    
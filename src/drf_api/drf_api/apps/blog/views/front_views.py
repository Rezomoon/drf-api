from django.http import JsonResponse
from django.shortcuts import render
from drf_api.apps.blog.models import Blog
from drf_api.apps.blog.serializers.front_ser import BlogSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def blog_view(request)  : 
    if request.method == "GET" : 
        blog_list = Blog.objects.all()
        serializer  = BlogSerializer( blog_list, many = True).data
        return JsonResponse(
            {
                'data' : serializer
            }
        )
    elif request.method == "POST" :
        print(request)
        data = JsonResponse().parse(request) # Baraye Ine k Data Daryafti ro parser konim
        print(data)
        
        serializer = BlogSerializer(data)

        if serializer.is_valid() :
            serializer.save()
            return JsonResponse (
                {
                    'data' : serializer.data
                }
            )
        else : 

            return JsonResponse(
                {
                    "data" :serializer.errors
                }
            ) 
@csrf_exempt        
def blog_detail_view(request , blog_id) : 

    blog = Blog.objects.get(id = blog_id)

    if request.method == "GET" : 
        serializer = BlogSerializer(blog)
        return JsonResponse({
            "data" : serializer.data
        })
    if request.method == "DELETE" : 
        blog.delete()
        return JsonResponse({
            "data" : "BLOG DELETED"
        })
    if request.method == "PUT" :

        data = JSONParser().parse(request)


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
    
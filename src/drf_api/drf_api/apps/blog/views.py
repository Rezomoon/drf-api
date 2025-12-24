from django.http import JsonResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog_view(request)  : 
    if request.method == "GET" : 
        blog_list = Blog.objects.all()
        return JsonResponse(
            {
                'data' : blog_list
            }
        )
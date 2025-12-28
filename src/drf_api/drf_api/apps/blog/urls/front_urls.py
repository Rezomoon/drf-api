from django.urls import path
from drf_api.apps.blog.views.front_views import blog_view , blog_detail_view

#

urlpatterns = [
    path("" , blog_view   ) , 
    path("<int:blog_id>/" , blog_detail_view) ,
]
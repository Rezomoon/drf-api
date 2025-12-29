from django.urls import path
from drf_api.apps.blog.views.front_views import blog_view , blog_detail_view , BlogDetails , BlogList

#

urlpatterns = [
    
    path("" , blog_view   ) , 
    path("<int:blog_id>/" , blog_detail_view) ,

    # Class Based Views : 

    path("cbv/" , BlogList.as_view()) , 
    path("cbv/<int:pk>/" , BlogDetails.as_view()) , 
    
]
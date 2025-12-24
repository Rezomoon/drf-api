from django.urls import path
from drf_api.apps.blog.views import blog_view
#

urlpatterns = [
    path("" , blog_view   )
]
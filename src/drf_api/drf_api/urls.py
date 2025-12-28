"""
URL configuration for drf_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include



# Tips : 
# 1. # baraye estefadeh az masiri digar az include estefadeh mishavd !
account_back_url = [
    path ("accounts/" , include("drf_api.auth.accounts.urls.back_urls")) ,  # Tip : Hatman Adrees dehi bayad az aval bashad Yani drf_api ham bayad bashe
]

blog_front_url = [
    path("blog/" , include("drf_api.apps.blog.urls.front_urls"))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/" , include("auth.accounts.urls.back_urls")) 
] + account_back_url + blog_front_url
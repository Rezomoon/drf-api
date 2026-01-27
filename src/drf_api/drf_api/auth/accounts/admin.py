from django.contrib import admin
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType

from .models import Profile

# Register your models here.
User = get_user_model()

class AdminUserModel(admin.ModelAdmin) : 
    list_display = ("id" , "email")

class AdminProfileModel(admin.ModelAdmin) : 
    list_display = ("id", "first_name", "last_name", "user")
admin.site.register(Profile , AdminProfileModel)
admin.site.register(User , AdminUserModel)
admin.site.register(LogEntry)
admin.site.register(ContentType)
from django.contrib import admin
from .models import Blog
# Register your models here.

# @admin.register(Blog)
# class AdminBlog(admin.ModelAdmin) :
#     list_display = ("title" , "content" , "created_by" , "created_at" , "updated_by" , "updated_at")

# TIPS : B 2 ravesh mishe anjam dad admin pannel ro :


class AdminBlogModel(admin.ModelAdmin) :
    list_display = ("id" , "status", "title", "author", "is_active")


admin.site.register(Blog,AdminBlogModel)
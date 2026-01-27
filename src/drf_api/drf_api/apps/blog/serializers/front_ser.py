from rest_framework import serializers
from drf_api.apps.blog.models import Blog
from drf_api.libs.db.models import AudiTableModel
#
class AudiTableModelSerializer(serializers.ModelSerializer) :
    class Meta : 
        model  = AudiTableModel
        fields   = "__all__"



class BlogSerializer (serializers.ModelSerializer) :
    class Meta : 
        model   = Blog
        fields  = [
            "id" , 
            "title" , 
            "content" ,
            "allow_comments" ,
            "is_active" ,
            "allow_update" ,
            "slug" ,
            "status" , 
            "author" ,
            "created_at" , 
            "updated_at" , 
        ]
        read_only_fields  = [
            "id",
            "slug",
            "created_at",
            "updated_at",
        ]
class BlogCreateSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Blog
        fields = [
            "title",
            "content",
            "author",
        ]
class BlogUpdateSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model   = Blog
        fields  = [
            "title",
            "content",
            "status",
            "is_active" ,
            "allow_comments" ,
        ]
class AuditSerializer(serializers.ModelSerializer)  : 
    class Meta : 
        model   = AudiTableModel
        fields  = "__all__"



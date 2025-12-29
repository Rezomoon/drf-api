from rest_framework import serializers
from drf_api.apps.blog.models import Blog
#

class BlogSerializer(serializers.Serializer) : 

    id  = serializers.IntegerField()
    title =  serializers.CharField ()
    slug  = serializers.SlugField()
    content = serializers.CharField()
    is_active =serializers.BooleanField()
    
    created_at  = serializers.DateTimeField()

    def create(self, validated_data):
        obj = Blog.objects.create(**validated_data) # vlidated_data => title=validated_data['title'] , slug = validated_dat['slug'] 
        obj.save()
        return obj
    def update(self, instance, validated_data):

        instance.title  = validated_data.get("title" , instance.title) # validated data yek dictationary hastesh k ba get b data hash dastressi peyda mikonim va etelaate daryafti hastesh
        instance.content = validated_data.get("content" , instance.content)# parametre dovom vorodi get(,instance.slug) => baraye ine k agar dar validated_data field morde nazar peyda nashod ya aresal nashode bood 
        # biad va hamon data va field ghabli ro estefadeh kone !
        instance.slug    = validated_data.get("slug" , instance.slug) 
        instance.is_active = validated_data.get("is_active" , instance.is_active)
        instance.save()
        return instance
        # return super().update(instance, validated_data)

class BlogModelSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Blog
        fields = "__all__"
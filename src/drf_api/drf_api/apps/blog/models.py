from django.db import models
from django.contrib.auth import get_user_model
from drf_api.libs.db.models import AudiTableModel

# Create your models here.
User = get_user_model()

class Blog(AudiTableModel) : 
    title = models.CharField(max_length=200 , null=True , blank= True)
    content = models.TextField()
    slug  = models.SlugField(max_length=200 , unique= True) # ?
    author = models.ForeignKey(User  , on_delete= models.CASCADE  , related_name="blog")

    is_active = models.BooleanField(default=True)
    allow_update = models.BooleanField(default=True)

    # created_time and Updated Time b sorate digar bayad sakhte shavad !

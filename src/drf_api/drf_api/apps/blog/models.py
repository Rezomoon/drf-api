from django.db import models

from drf_api.libs.db.models import AudiTableModel
import uuid
from django.utils.text import slugify
from django.conf import settings


# Create your models here.

# Tip : we refreing user like this for example for query but for fk in models we refreing by settings.AUTH_USER_MODEL
# from django.contrib.auth import get_user_model
# User = get_user_model()

class Blog(AudiTableModel) : 



    class StatusChoices (models.TextChoices) : 

        Draft       = "Draft"

        Published   = "Published"

        Archived    = "Archived"

    status  = models.CharField(max_length=16 , choices=StatusChoices.choices ,default=StatusChoices.Draft )

    id      = models.UUIDField(default=uuid.uuid4 , unique= True , primary_key=True , editable= False)
    
    title   = models.CharField(max_length=200 , null=True , blank= True)
    content = models.TextField()
    slug    = models.SlugField(max_length=200 , unique= True) # ?
    author  = models.ForeignKey(settings.AUTH_USER_MODEL  , on_delete= models.CASCADE  , related_name="blog")

    allow_comments = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    allow_update = models.BooleanField(default=True)

    # created_time and Updated Time b sorate digar bayad sakhte shavad !
    def save(self,*args, **kwargs):
        if not self.slug and self.title : 
            original_slug = slugify(self.title)
            queryset = Blog.objects.filter(slug__iexact=original_slug)
            if self.id:
                queryset = queryset.exclude(id=self.id)
                
            if queryset.exists():
                self.slug = f"{original_slug}-{uuid.uuid4().hex[:8]}"
            else:
                self.slug = original_slug
                
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} "
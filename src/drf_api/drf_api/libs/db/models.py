from django.db import models
from django.conf import settings


class AudiTableModel(models.Model) :
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null= True , related_name= "created" , editable=False)
    created_at = models.DateTimeField(auto_now_add=True , null= True)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null=True ,  related_name="updated" , editable=False)
    updated_at = models.DateTimeField(auto_now=True ,null= True)

    class Meta : 
        abstract = True
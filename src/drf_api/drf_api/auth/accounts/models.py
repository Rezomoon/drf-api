from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.


class UserManager(BaseUserManager) : 

    def create_user(self  , email , password = None) : 

        if not email :
            raise ValueError("email not found")
        
        user = self.model(
            email = self.normalize_email(email)
        )

        user.set_password(password)

        user.save() # using = self._db

        return user
    
    def create_superuser(self , email , password) :

        user = self.create_user(email , password) 

        user.is_admin = True

        user.save()

        return user

class User(AbstractBaseUser) : 
    email           = models.EmailField( editable=False , max_length=254 , unique=True , verbose_name="email address") ,  
    is_active       = models.BooleanField( default=True , )
    is_admin        = models.BooleanField(default=False)

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []

    @property
    def is_staff(self) : # Yani Aya Karmand hastesh karbar ya na # Yani harkarbar k admin bashe staff ham bashad 
        return self.is_admin

    def has_module_perms(self , app_label) : # I think its for Permissions
        return True
    
    def has_perm(self , perm, obj = None) : # I think its for Permissions
        return True
    
    objects = UserManager()
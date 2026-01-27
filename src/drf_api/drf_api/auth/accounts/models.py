from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
import uuid
from drf_api.libs.db.models import AudiTableModel
from django.utils.translation import gettext_lazy as _ # ?? ask ai

from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager) : 

    def create_user(self  , email , password = None , **extra_fields) : 
        """
        Create and save a user with the given email and password.
        """

        if not email :
            raise ValueError(_("email not found"))
        
        email = self.normalize_email(email)

        user = self.model(
            email = email  , 
            **extra_fields
        )

        user.set_password(password)

        user.save() # using = self._db

        return user
    
    def create_admin(self  , email , password ,  **extra_fields) : 
      
    #   Docstring for create_admin      
    #   Create admin role 

        extra_fields.setdefault("is_active" , True )
        extra_fields.setdefault("is_admin" , True)

        if extra_fields.get("is_admin") is not True :
            return ValueError("User Must Be is_admin=True .")
        
        user = self.create_user(email , password , **extra_fields)

        user.is_admin = True

        user.save(using=self._db)

        return user
      

    
    def create_superuser(self , email , password , **extra_fields) :
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault("is_staff" , True )
        extra_fields.setdefault("is_superuser" , True )
        extra_fields.setdefault("is_active" , True )

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(email , password , **extra_fields) 

        user.is_admin = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser) : # PermissionsMixin

    id              = models.UUIDField(default     =uuid.uuid4 ,
                        unique      = True ,
                        primary_key =True ,  #  ba in kare index kardan ro ham anjam midim !
                        db_index    =True ,
                        editable=False ,
                        )
    
    email           = models.EmailField( 
        max_length=254 , 
        unique=True , 
        verbose_name="email address" , ) 
    
    
    date_joined     = models.DateTimeField(auto_now_add=True , null = True )

    is_verified     = models.BooleanField(default=False)
    is_active       = models.BooleanField( default=True )
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []

    # @property
    # def is_staff(self) : # Yani Aya Karmand hastesh karbar ya na # Yani harkarbar k admin bashe staff ham bashad 
    #     return self.is_admin

    def __str__(self):
        return self.email
    def has_module_perms(self , app_label) : # I think its for Permissions
        return True
    
    def has_perm(self , perm, obj = None) : # I think its for Permissions
        return True
    
    objects = UserManager()


class Profile (models.Model) : 

    first_name      = models.CharField(max_length=160) 

    last_name       = models.CharField(max_length=160) 

    bio             = models.TextField(null=True , blank=True)

    user      = models.OneToOneField( 
                                    settings.AUTH_USER_MODEL ,  # TIp : When we want to use fk in models we should use refreing user model by setting.AUTH_USER_MODEL
                                    on_delete=models.CASCADE ,  # Agar Karbar Hazf shavad Profile ham hazf mishavad !
                                    related_name="profile" ,     # user.profile => baraye dastresie maxkos va b shoma ejazeh midadhd az tarighe sheie aslie b sheye farie dastresi dashte bashim  
                                    )
    # avatar      =  Bayad yek field image baraye axe profile ezafeh beshe


    def __str__(self):

        return self.first_name + " " +self.last_name
    

    def save(self, *args , **kwargs) :

        self.first_name = self.first_name.lower()

        self.last_name  = self.last_name.lower()

        return super().save(*args , **kwargs)

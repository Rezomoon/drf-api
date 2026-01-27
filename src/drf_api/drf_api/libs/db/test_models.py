from django.test import TestCase 
from rest_framework.test import APITestCase
from .models import AudiTableModel
from django.contrib.auth import get_user_model
from drf_api.apps.blog.models import Blog
# Create Your Test Here

User = get_user_model()

class UserFactory :
    """

    Docstring for UserFactory
    Create Instance User with AbstarctBaseUser 

    """
    counter = 0

    @classmethod
    def create(cls , email = None , password = "password") :

        cls.counter += 1
        if not email :
            email = f"user{cls.counter}@example.com"
            
        user = User.objects.create_user(email=email , password=password)

        return user

class TestAudiTableModel(TestCase) : 
    def test_created_at_and_updated_at_are_set(self):
        """
        Docstring for test_created_at_and_updated_at_are_set
        
        :param self: It Check The updated_at and created_at fields in AuditTable after create one blog

        """

        user = UserFactory.create()
        blog = Blog.objects.create(
            status  = "Draft" , 
            title   = "Title" , 
            content = "content" ,
            slug    = "slug" , 
            author  = user ,
            allow_comments  = True , 
            is_active       = True , 
            allow_update    = True
        )
        self.assertIsNotNone(blog.created_at)
        self.assertIsNotNone(blog.updated_at)
    def test_blog_updated_at(self) :
        """
        Docstring for test_blog_updated_at
        
        :param self:  It Check AudiTable Model updated_at field after Change or Update blog fields !
        
       """
        user = UserFactory.create()

        blog = Blog.objects.create(
            status  = "Draft" , 
            title   = "Title" , 
            content = "content" ,
            slug    = "slug" , 
            author  = user ,
            allow_comments  = True , 
            is_active       = True , 
            allow_update    = True
        )

        old_blog = blog.updated_at

        blog.title = "Title2"
        blog.save()

        blog.refresh_from_db()

        self.assertNotEqual(old_blog , blog.updated_at)

class BlogCreateAuditTest(APITestCase) : 
    """
    Docstring for BlogCreateAuditTest

    We Want To Test created_by and updated_by and it need user that auth and it should be in API
    So We Sould user and test by API For This Field !

    """

    def test_created_by_is_set_from_request_user(self) : 
        """
        Docstring for test_created_by
        
        :param self: We Want To Test Http and API request It Mean :
        - authentication
        - request.user
        - view
        - serializers
        And Cuase created_by get from request :
        So Wew Should Use APITestCase 
        And Cause The User Dont Send Id or User data from front and in API Data and we should get it from request 
        So We Create Simple API Request For Test Created_by

        """
        print("TESTING : ")
        user = UserFactory.create()
        self.client.force_authenticate(user = user)  
        # It Mean that for client boject and  all of the next request login this user that we pass it (Fast Test , Focous On behavior , Delete Noise)
        # We want to test audit (no JWT)
        response = self.client.post(
            path = "/blog/cbv/" ,
            data = {
            "content"   : "content" ,
            "slug"      : "slug" ,
            }
        ) 
        print(response)
        blog = Blog.objects.get(id = response.data["id"])

        self.assertEqual(blog.created_by , user)


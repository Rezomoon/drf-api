from django.test import TestCase
from django.contrib.auth import get_user_model 
from drf_api.auth.accounts.models import Profile
from drf_api.libs.db.test_models import UserFactory


# Create Your Tests Here 
User = get_user_model()


class ProfileTest(TestCase) :

    def test_profile_creation(self) : 

        user    = UserFactory.create()
        profile     = user.profile
        profile.first_name  = "FIrstName"
        profile.last_name   = "LaStName"
        profile.bio         = "Bio"
        profile.save()

        profile.refresh_from_db() # It Clean The RAM and Refresh the Query and sync object with new Data
        

        
        self.assertEqual(profile.first_name , "firstname")
        self.assertEqual(profile.last_name , "lastname")
        self.assertEqual(profile.bio , "Bio")
        self.assertEqual(profile.user , user)


class ProfileSignalsTest(TestCase) : 
    def test_profile_created_signals(self):
        """
        Docstring for test_profile_created_signals
        
        :param self: Description
        Its For Check After Create User(Here we use : UserFactory) => Profile Created With Signal or no !

        """

        user = UserFactory.create()
        self.assertIsNotNone(user.profile)







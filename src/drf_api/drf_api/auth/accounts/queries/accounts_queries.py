from django.contrib.auth import get_user_model

# Queries
User = get_user_model()

def UserListQueries():

    query = User.objects.all()
    
    return query
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Tips : 
# 1 . as_view() => chon bayad vorodi path yek tabe bashad baraye ejraye darkhast ha ba as_view() oon roo tabild b yek tabe mikonim
# Dar vaghe as_view yek nemone va instance az class misazad va tabe barmigardanad

# 2 . name=  => k dar enteha azash estefadeh mishavad b onvane yek barchasb ya yek esme mostaad (ALLIAS) estefadeh mishavad ta az tekrar jelo giri shavad 
# Yani agar chand ja dashtim az adrese b sorate HARDCODEING estefadeh mikardim agar k adres va endpoint avaz shavad bayad dar tamam jahayee k barname hastesh
# Avazesh konim vali ba estefadeh az name faghat esmesh name ro avaz mikonim !


urlpatterns = [
    path ("api/token/" , TokenObtainPairView.as_view() , name='token_obtain_pair') , 
    path("api/token/refresh/" , TokenRefreshView.as_view() , name = 'token_refresh') , 
]

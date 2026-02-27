from django.urls import  path
from b_auth import views



urlpatterns = [
    path('',views.home,name='home')
    
]

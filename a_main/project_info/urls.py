from django.urls import path
from . import views


urlpatterns = [
    path('',views.project_info,name='project_info')
    
]

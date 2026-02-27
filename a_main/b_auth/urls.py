from django.urls import  path
from b_auth import views



urlpatterns = [
    path('',views.add_patient,name='home'),
    path('view_patients/',views.view_patient,name='view_patient'),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register_page,name='register'),
    path('logout/',views.logout_page,name='logout')
]

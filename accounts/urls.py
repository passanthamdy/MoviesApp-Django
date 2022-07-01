from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login", views.user_login, name="login")    ,
    path("logout", views.user_logout, name= "logout"),
   

]
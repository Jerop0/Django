from django.urls import path
from . import views

urlpatterns = [
    path('', views.registeration, name='Registeration'),
    path('login/', views.registeration_login, name='Registeration_Login'),
    path('signup/', views.registeration_signup, name='Registeration_Signup'),
]

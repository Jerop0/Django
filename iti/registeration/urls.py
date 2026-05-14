from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Registeration"),
    path('login/', views.UserLogin.as_view(), name="Registeration_Login"),
    path('logout/', views.UserLogout.as_view(), name="Registeration_Logout"),
    path('register/', views.Register.as_view(), name="Registeration_Signup"),
]

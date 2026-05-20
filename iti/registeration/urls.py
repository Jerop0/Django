from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home, name="Registeration"),
    path('login/', views.UserLogin.as_view(), name="Registeration_Login"),
    path('logout/', views.UserLogout.as_view(), name="Registeration_Logout"),
    path('register/', views.Register.as_view(), name="Registeration_Signup"),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

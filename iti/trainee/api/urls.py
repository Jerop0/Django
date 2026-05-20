from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('members', views.StudentViewset, basename='members')

urlpatterns = [
    path('', include(router.urls)),
]

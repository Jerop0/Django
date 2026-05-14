from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='Course_List'),
    path('add/', views.course_add, name='Course_Add'),
    path('details/<int:id>/', views.course_details, name='Course_Details'),
    path('update/<int:id>/', views.course_update, name='Course_Update'),
    path('delete/<int:id>/', views.course_delete, name='Course_Delete'),
]

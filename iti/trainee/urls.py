from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='Trainee_List'),
    path('add/', views.trainee_add, name='Trainee_Add'),
    path('details/<int:id>/', views.trainee_details, name='Trainee_Details'),
    path('update/<int:id>/', views.trainee_update, name='Trainee_Update'),
    path('delete/<int:id>/', views.trainee_delete, name='Trainee_Delete'),
]

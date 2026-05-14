from django.urls import path
from . import views

urlpatterns = [
    path('', views.TraineeList.as_view(), name='Trainee_List'),
    path('add/', views.TraineeAdd.as_view(), name='Trainee_Add'),
    path('add-form/', views.TraineeAddGeneric.as_view(), name='Trainee_add_form'),
    path('details/<int:id>/', views.trainee_details, name='Trainee_Details'),
    path('update/<int:id>/', views.trainee_update, name='Trainee_Update'),
    path('delete/<int:id>/', views.trainee_delete, name='Trainee_Delete'),
    path('soft-delete/<int:id>/', views.trainee_soft_delete, name='Trainee_Soft_Delete'),
]

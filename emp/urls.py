

from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('create/', views.emp_create, name='emp_create'),
    path('edit/', views.emp_edit, name='emp_edit'),
    path('delete/', views.emp_delete, name='emp_delete'),
]
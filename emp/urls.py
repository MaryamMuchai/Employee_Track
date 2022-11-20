from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('create/', views.create_emp, name='create_emp'),
    path('edit/', views.edit_emp, name='edit_emp'),
    path('delete/', views.delete_emp, name='delete_emp'),

    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")

]
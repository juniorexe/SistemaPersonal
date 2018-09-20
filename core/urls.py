from django.contrib import admin
from django.urls import path
from .views import home, cadastro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('cadastro/', cadastro, name="cadastro"),
]
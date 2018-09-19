from django.contrib import admin
from django.urls import path
from .views import home, cadastro

urlpatterns = [
    path('', home, name="home"),
    path('cadastro/', cadastro, name="cadastro"),
]
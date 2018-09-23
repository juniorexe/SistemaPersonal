from django.contrib import admin
from django.urls import path
from .views import home, my_logout, cadastro, listarAlunos


urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="my_logout"),
    path('cadastro/', cadastro, name="cadastro"),
    path('todosAlunos/', listarAlunos, name="listarAlunos"),
]
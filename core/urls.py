from django.contrib import admin
from django.urls import path
from .views import home, my_logout
from .views import cadastrarAluno, avaliarAluno, listarAlunos

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="my_logout"),
    path('cadastro-de-aluno/', cadastrarAluno, name="cadastrarAluno"),
    path('avaliacao/<int:id>/', avaliarAluno, name="avaliarAluno"),
    path('todos-os-alunos/', listarAlunos, name="listarAlunos"),
]
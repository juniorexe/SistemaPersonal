from django.contrib import admin
from django.urls import path
from .views import home, my_logout
from .views import cadastrarAluno, editarAluno, excluirAluno
from .views import avaliarAluno, listarAlunos

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="my_logout"),
    path('cadastro-de-aluno/', cadastrarAluno, name="cadastrarAluno"),
    path('editar-aluno/<int:id>', editarAluno, name="editarAluno"),
    path('excluir-aluno/<int:id>', excluirAluno, name="excluirAluno"),
    path('avaliacao/', avaliarAluno, name="avaliarAluno"),
    path('todos-os-alunos/', listarAlunos, name="listarAlunos"),
]
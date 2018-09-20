from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Aluno, Medidas


def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro_aluno.html')

def novo_cadastro(request):
    objeto = request.POST
    

def calcula_imc(aluno):
    peso = aluno.peso
    altura = aluno.altura
    
    imc = (peso/pow(altura))

    return imc

def consulta_medidas(request):
    aluno = request.GET.get('idAluno', None)
    calcAluno = Aluno.objects.filter(id=idAluno)
    imcAluno = calcula_imc(calcAluno)

    return render(request, 'avaliacao.html', {'imcAluno' : imcAluno})


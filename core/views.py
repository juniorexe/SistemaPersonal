from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Aluno, Medidas
from .forms import AlunoForm


def my_logout(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    return render(request, 'index.html')

def cadastro(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastro_aluno.html', {'form': form})

def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

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


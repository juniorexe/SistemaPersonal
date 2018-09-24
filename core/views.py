from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Aluno, Medidas
from .forms import AlunoForm, MedidasForm


def my_logout(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    return render(request, 'index.html')

def cadastrarAluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastro_aluno.html', {'form': form})

def avaliarAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = MedidasForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'avaliacao.html', {'form': form})

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


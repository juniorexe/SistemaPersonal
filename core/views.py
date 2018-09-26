from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Aluno, Medidas
from .forms import AlunoForm, AlunoFormCompleto, MedidasForm


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

def editarAluno(request, id):
    alunoEditar = get_object_or_404(Aluno, pk=id)
    form = AlunoFormCompleto(request.POST or None,  instance=alunoEditar)

    if form.is_valid():
        form.save()
        return redirect('listarAlunos')
    return render(request, 'cadastro_aluno.html', {'form': form})

def excluirAluno(request, id):
    alunoDeletar = get_object_or_404(Aluno, pk=id)
    if request.method == 'POST':
        alunoDeletar.delete()
        return redirect('listarAlunos')
    return render(request, 'lista_alunos.html', {'alunoDeletar': alunoDeletar})

def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def avaliarAluno(request):
    form = MedidasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'avaliacao.html', {'form': form})

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


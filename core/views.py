from django.shortcuts import render
from models import Aluno, Medidas

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


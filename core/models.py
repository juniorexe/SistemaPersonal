from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=12)
    idade = models.IntegerField
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

class Medidas(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    pescoco = models.DecimalField(max_digits=5, decimal_places=2)
    toraxica = models.DecimalField(max_digits=5, decimal_places=2)
    costas = models.DecimalField(max_digits=5, decimal_places=2)
    braco = models.DecimalField(max_digits=5, decimal_places=2)
    anteBraco = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    abdominal = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    coxaEsquerda1 = models.DecimalField(max_digits=5, decimal_places=2)
    coxaEsquerda2 = models.DecimalField(max_digits=5, decimal_places=2)
    coxaEsquerda3 = models.DecimalField(max_digits=5, decimal_places=2)
    coxaDireita1 = models.DecimalField(max_digits=5, decimal_places=2)
    coxaDireita2 = models.DecimalField(max_digits=5, decimal_places=2)
    coxaDireita3 = models.DecimalField(max_digits=5, decimal_places=2)
    pantuEsq = models.DecimalField(max_digits=5, decimal_places=2)
    pantuDir = models.DecimalField(max_digits=5, decimal_places=2)

    alunoRelacionado = models.OneToOneField(Aluno, null=False, blank=False, on_delete=models.CASCADE)


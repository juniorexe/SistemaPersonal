from django.forms import ModelForm
from .models import Aluno, Medidas

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email', 'dtNascimento']

class MedidasForm(ModelForm):
    class Meta:
        model = Medidas
        #fields = ['peso', 'altura', 'pescoco', 'toraxica', 'costas', 'braco', 'anteBraco', 'cintura', 'abdominal', 'quadril', 'coxaEsquerda1', 'coxaEsquerda2', 'coxaEsquerda3', 'coxaDireita1', 'coxaDireita2', 'coxaDireita3', 'pantuEsq', 'pantuDir']
        fields = '__all__'

class AlunoFormCompleto(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

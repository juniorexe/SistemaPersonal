from django.forms import ModelForm
from .models import Aluno, Medidas

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email', 'dtNascimento']

class MedidasForm(ModelForm):
    class Meta:
        model = Medidas
        fields = '__all__'

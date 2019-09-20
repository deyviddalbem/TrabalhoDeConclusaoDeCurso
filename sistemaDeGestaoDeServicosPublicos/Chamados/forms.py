from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orgao, TipoChamado

class CadastroTiposChamadosForm(forms.ModelForm):
     class Meta:
        model = TipoChamado
        fields = '__all__'

class AtualizarTiposChamadosForm(forms.ModelForm):
    class Meta:
        model = TipoChamado
        fields = '__all__'

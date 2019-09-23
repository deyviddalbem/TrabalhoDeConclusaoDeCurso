from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orgao, TipoChamado, Status, OcorrenciasChamado, Chamado

class CadastroTiposChamadosForm(forms.ModelForm):
     class Meta:
        model = TipoChamado
        fields = '__all__'

class AtualizarTiposChamadosForm(forms.ModelForm):
    class Meta:
        model = TipoChamado
        fields = '__all__'

class CriarStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class AtualizarStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class CadastrarOcorrenciasChamadoForm(forms.ModelForm):
    class Meta:
        model = OcorrenciasChamado
        fields = '__all__'
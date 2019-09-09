from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orgao


class CadastroOrgaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroOrgaoForm, self).__init__(*args, **kwargs)
        self.fields['nomeOrgao'].widget.attrs = {
        'class': 'form-group form-control', 'type': 'text', 'placeholder': 'digite o nome da Secretaria'}
        self.fields['descricao'].widget.attrs = {
        'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe uma Descricao'}
        self.fields['emailOrgao'].widget.attrs = {'class': 'form-group form-control',
                                              'type': 'text', 'placeholder': 'informe o email da secretaria a ser cadastrada'}
        self.fields['nomeResponsavelOrgao'].widget.attrs = {
        'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o nome do responsável pela secretaria'}
        self.fields['telefoneOrgao'].widget.attrs = {
        'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o telefone da secretaria a ser cadastrada'}
        self.fields['enderecoOrgao'].widget.attrs = {
        'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o endereco da secretaria a ser cadastrada'}

    class Meta:
        model = Orgao
        fields = '__all__'

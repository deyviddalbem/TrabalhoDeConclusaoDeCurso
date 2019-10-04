from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orgao, TipoLotacao, Lotacao
from Chamados.models import Chamado, OcorrenciasChamado


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

class CadastroTipoLotacaoForm(forms.ModelForm):
    class Meta:
        model = TipoLotacao
        fields = '__all__'

class CadastroLotacaoForm(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = '__all__'

class AtualizarLotacaoForm(forms.ModelForm):
    class Meta:
        model = Lotacao
        fields = '__all__'

class atualizarChamadosOrgaoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'
        exclude = ('idOrgao','idTipoChamado', 'idUsuario', 'idEndereco', 'numeroProtocolo')

class CadastrarOcorrenciasChamadoForm(forms.ModelForm):
    class Meta:
        model = OcorrenciasChamado
        fields = '__all__'
     
        
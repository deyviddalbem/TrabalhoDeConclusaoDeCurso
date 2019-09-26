
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Telefone, Endereco


##### Formulário para cadastro de usuário #####
class PessoaUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(PessoaUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Informe o  Nome'}
        self.fields['last_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Informe o Sobrenome'}
        #self.fields['username'].widget.attrs = {'class':'form-group form-control','type':'text','placeholder':'CPF'}
        self.fields['username'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'mail', 'placeholder': 'Insira nome de usuário'}
        self.fields['password1'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'password', 'placeholder': 'Insira a Senha'}
        self.fields['password2'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'password', 'placeholder': 'Repita a senha'}

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2')
        labels = {'username': 'Nome de Usuário'}


class PessoaUserFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PessoaUserFormUpdate, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Nome'}
        self.fields['last_name'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'Sobrenome'}
        self.fields['email'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'mail', 'placeholder': 'E-mail'}
        self.fields['username'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'mail', 'placeholder': 'username'}

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class CadastroTelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'


class CadastroEnderecoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroEnderecoForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'digite seu CEP'}
        self.fields['logradouro'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe seu logradouro'}
        self.fields['enderecoNumero'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': ' insira o Número do imóvel'}
        self.fields['complemento'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o Complemento'}
        self.fields['bairro'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o Bairro'}
        self.fields['observacao'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'insira uma Observação, se houver'}
        self.fields['municipio'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'insira o municipio'}
        self.fields['estado'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'text', 'placeholder': 'informe o estado'}
        self.fields['idPessoa'].widget.attrs = {
            'class': 'form-group form-control', 'type': 'hidden'}

    class Meta:
        model = Endereco
        fields = '__all__'


class DadosUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
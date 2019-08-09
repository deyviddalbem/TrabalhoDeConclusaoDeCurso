
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Telefone



class PessoaUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(PessoaUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {'class':'form-group form-control','type':'text','placeholder':'Nome'}
        self.fields['last_name'].widget.attrs = {'class':'form-group form-control','type':'text','placeholder':'Sobrenome'}
        #self.fields['username'].widget.attrs = {'class':'form-group form-control','type':'text','placeholder':'CPF'}
        self.fields['username'].widget.attrs = {'class':'form-group form-control','type':'mail','placeholder':'E-mail'}
        self.fields['password1'].widget.attrs = {'class':'form-group form-control','type':'password','placeholder':'Senha'}
        self.fields['password2'].widget.attrs = {'class':'form-group form-control','type':'password','placeholder':'Repita a senha'}
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1', 'password2')
        labels = {'username':'email'}

class CadastroTelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'   
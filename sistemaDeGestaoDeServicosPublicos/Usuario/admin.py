from django.contrib import admin
from django.contrib.auth.models import User
from .models import TipoTelefone
from .models import Telefone
from .models import Endereco



#from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'senha',)
    list_filter = []

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idTipoTelefone', 'numero')
    list_filter = ['idPessoa', 'idTipoTelefone']

class TipoTelefoneAdmin(admin.ModelAdmin):
    list_display = ('descricao', )
    list_filter = ['id', 'descricao']

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'enderecoNumero', 'bairro', 'complemento', 'observacao', 'municipio', 'estado', 'idPessoa' )
    list_filter = ['id','cep', 'logradouro', 'enderecoNumero', 'bairro', 'complemento', 'observacao', 'municipio', 'estado', 'idPessoa']

admin.site.register(Telefone,TelefoneAdmin)
admin.site.register(TipoTelefone,TipoTelefoneAdmin)
admin.site.register(Endereco,EnderecoAdmin)



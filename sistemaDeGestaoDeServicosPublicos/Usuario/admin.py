from django.contrib import admin
from django.contrib.auth.models import User
from .models import TipoTelefone
from .models import Telefone
from .models import Estado
from .models import Municipio
from .models import Bairro
from .models import Rua



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

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nomeEstado', )
    list_filter = ['id', 'nomeEstado']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nomeMunicipio','idEstado' )
    list_filter = ['id','nomeMunicipio', 'idEstado']

class BairroAdmin(admin.ModelAdmin):
    list_display = ('nomeBairro',)
    list_filter = ['id','nomeBairro','idMunicipio']

class RuaAdmin(admin.ModelAdmin):
    list_display = ('cepRua', 'nomeRua', 'idBairro',)
    list_filter = ['id','cepRua','nomeRua', 'idBairro']


admin.site.register(Telefone,TelefoneAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(TipoTelefone,TipoTelefoneAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(Bairro,BairroAdmin)
admin.site.register(Rua,RuaAdmin)

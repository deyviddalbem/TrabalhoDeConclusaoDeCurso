from django.contrib import admin
from django.contrib.auth.models import User
from .models import Orgao
from .models import Lotacao
from .models import TipoLotacao



#from .models import Pessoa


class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomeOrgao', 'descricao', 'emailOrgao', 'nomeResponsavelOrgao','idEndereco', 'idTelefone', 'idTipoChamado',)
    list_filter = ['id', 'nomeOrgao', 'descricao']

class TipoLotacaoAdmin(admin.ModelAdmin):
    list_display = ('id','descricao',)
    list_filter = ['id','descricao']

class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('id','observacao','idTipoLotacao', 'idUsuario', 'idOrgao')
    list_filter = ['id']

admin.site.register(Orgao,OrgaoAdmin)
admin.site.register(TipoLotacao,TipoLotacaoAdmin)
admin.site.register(Lotacao,LotacaoAdmin)



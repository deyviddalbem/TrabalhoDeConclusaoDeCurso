from django.contrib import admin
from .models import TipoChamado
from .models import Status
from .models import OcorrenciasChamado
from .models import Chamado

class TipoChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricaoTipoChamado','idOrgao')
    list_filter = ['id', 'descricaoTipoChamado']

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_filter = ['id', 'descricao']

class OcorrenciasChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricaoOcorrenciasChamado')
    list_filter = ['id', 'descricaoOcorrenciasChamado']

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id','dataAbertura','dataConclusao','numeroProtocolo','observacao','observacaoOrgao','idStatus','idOrgao','idTipoChamado','idUsuario','idOcorrenciasChamado','idEndereco')
    list_filter = ['id', 'numeroProtocolo', 'dataAbertura','dataConclusao','idStatus' ]
    
admin.site.register(TipoChamado,TipoChamadoAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(OcorrenciasChamado, OcorrenciasChamadoAdmin)
admin.site.register(Chamado, ChamadoAdmin)

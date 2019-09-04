from django.contrib import admin
from .models import TipoChamado

class TipoChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricaoTipoChamado','idOrgao')
    list_filter = ['id', 'descricaoTipoChamado']


admin.site.register(TipoChamado,TipoChamadoAdmin)
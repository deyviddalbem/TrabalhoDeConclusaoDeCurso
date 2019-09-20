from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

app_name = 'Chamados'

urlpatterns = [
    path('cadastrarTipoChamado/', views.CadastroTipoChamado, name='cadastro_tipo_chamado'),
    path('listarTiposDeChamado/', views.tiposChamadosList, name='lista_tipo_chamado'),
    path('atualizarTiposDeChamado/<int:pk>', views.atualizarTipoChamado, name='tipo_chamado_atualizar'),
    path('excluirTipoDeChamado/<int:pk>', views.DeletarTipoChamado.as_view(),name='tipo_chamado_deletar'),
    ####
    
]
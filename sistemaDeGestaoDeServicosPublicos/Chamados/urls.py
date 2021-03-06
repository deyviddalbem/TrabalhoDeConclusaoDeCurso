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
    path('cadastrarStatusChamado/', views.CadastrarStatus.as_view(), name='cadastro_status_chamado'),
    path('listarStatusChamado/', views.ListaStatus, name='lista_status_chamado'),
    path('atualizarStatusChamado/<int:pk>', views.atualizarStatus, name='status_atualizar'),
    path('excluirStatusChamado/<int:pk>', views.DeletarStatus.as_view(),name='status_deletar'),
    ####
    path('cadastrarChamado/', views.CadastroChamado, name='cadastro_chamado'),
    path('listarChamado/<int:pk>', views.ListChamados.as_view(), name='lista_chamado'),
    path('atualizarChamado/<int:pk>', views.atualizarChamado, name='atualiza_chamado'),
    path('<int:pk>/<int:statusChamado>', views.FiltrarChamados.as_view(), name='filtrar_chamados'),
    path('ajax-search/<str:search_string>', views.home_ajax_search, name='pesquisa'),
    path('Chamadodetalhado/<int:pk>', views.detalheChamado, name='chamado_detalhado'),

]
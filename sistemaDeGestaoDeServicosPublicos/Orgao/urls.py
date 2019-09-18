from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


app_name = 'Orgao'

urlpatterns = [
    #path('', views.index, name='index'),
    path('index_orgao/semosp',views.indexOrgao, name='orgao_index'),
    #path('index_orgao/', views.CriarCadastro.as_view(), name='orgao_index'),
    path('escolheLotacao/', views.retornaLotacao, name='retorna_Lotacao'),
    path('cadastrarOrgao/', views.CriarOrgao.as_view(), name='cadastro_orgao'),
    path('cadastrarTipoLotacao/', views.CadastrarTipoLotacao.as_view(), name='cadastro_Tipo_Lotacao'),
    path('OrgaoDados/', views.orgaoList, name='dados_orgao'),
    path('TiposLotacao/', views.TipoLotacaoList, name='tipos_lotacao'),
    path('orgao/atualizar/<int:idOrgao>', views.atualizaOrgao,name='orgao_atualizar'),
    path('orgao/atualizarTipoLotacao/<int:pk>', views.AtualizarTipoLotacao.as_view(),name='Tipo_lotacao_atualizar'),
    path('orgao/excluirTipoLotacao/<int:pk>', views.DeletarTipoLotacao.as_view(),name='tipo_lotacao_deletar'),
    path('cadastrarLotacao/', views.CadastroLotacao, name='cadastro_Lotacao'),
    path('listarLotacoes/', views.LotacaoList, name='lista_lotacao'),
    path('atualizarLotacao/<int:idLotacao>/alterar', views.atualiza_Lotacao, name='lotacao_atualizar'),
    path('orgao/excluirLotacao/<int:pk>', views.DeletarLotacao.as_view(),name='lotacao_deletar'),
]


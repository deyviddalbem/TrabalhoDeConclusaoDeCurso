from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views



urlpatterns = [
    path('index.html', views.index, name='index'),
    path('cadastrarUsuario/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('atualizarMeusDados/', views.AtualizarCadastro.as_view(), name='atualizarCadastro'),
    path('meusDados/', views.mostrarMeusDados, name='meusDados'),

    path('cadastroEndereco/', views.cadastroEndereco, name='cadastroEndereco'),
    path('meusEnderecos/', views.enderecosList, name='listaEnderecos'),
    path('enderecos/listar/<int:pk>',views.ListarEnderecos.as_view(), name='listar_enderecos'),
    #path('enderecos/listar/',views.enderecosList, name='enderecosList'),
    path('enderecos/excluir/<int:pk>', views.DeletarEndereco.as_view(),name='endereco_deletar'),
   
    path('cadastroTelefone/', views.CadastroTelefone, name='cadastroTelefone'),
    path('meusTelefones/', views.TelefonesList, name='listaTelefones'),
    path('meusTelefones/editar/<int:idTelefone>', views.atualizarMeusTelefones,name='telefone_atualizar'),
    path('meusTelefones/excluir/<int:pk>', views.DeletarTelefone.as_view(),name='telefone_deletar'),
    
  
    
]

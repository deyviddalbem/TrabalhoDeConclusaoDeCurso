from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views



urlpatterns = [
    path('index.html', views.index, name='index'),
    path('cadastrarUsuario/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('meusEnderecos/', views.enderecosList, name='listaEnderecos'),
    path('meusTelefones/', views.TelefonesList, name='listaTelefones'),
    path('meusTelefones/editar/<int:idTelefone>', views.atualizarMeusTelefones,name='telefone_atualizar'),
     path('meusTelefones/excluir/<int:pk>', views.DeletarTelefone.as_view(),name='telefone_deletar'),
    path('cadastroTelefone/', views.CadastroTelefone, name='cadastroTelefone'),
    path('cadastroEndereco/', views.CadastroEndereco, name='cadastroEndereco'),
    
]

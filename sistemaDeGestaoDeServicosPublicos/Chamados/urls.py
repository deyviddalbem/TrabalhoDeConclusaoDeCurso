from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

app_name = 'Chamados'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('cadastrarUsuario/', views.CriarCadastro.as_view(), name='cadastrar'),
]
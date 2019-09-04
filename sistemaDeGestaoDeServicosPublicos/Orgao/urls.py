from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views


app_name = 'Orgao'

urlpatterns = [
    #path('', views.index, name='index'),
    path('index_orgao/',views.indexOrgao, name='orgao_index'),
    #path('index_orgao/', views.CriarCadastro.as_view(), name='orgao_index'),
    path('escolheLotacao/', views.retornaLotacao, name='retorna_Lotacao'),
]

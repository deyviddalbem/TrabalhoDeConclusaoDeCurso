from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('Usuario/', include('Usuario.urls')),
    path('Chamados/', include('Chamados.urls')),
    path('Orgao/', include('Orgao.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('socialLogin/', include('social_django.urls', namespace='social')),
    path('', TemplateView.as_view(template_name='sistemaDeGestaoDeServicosPublicos/index1.html'), name="index"),

]

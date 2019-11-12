from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('Usuario/', include('Usuario.urls')),
    path('Chamados/', include('Chamados.urls')),
    path('Orgao/', include('Orgao.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='sistemaDeGestaoDeServicosPublicos/index1.html'), name="index"),
    path('auth/', include('social_django.urls', namespace='social')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

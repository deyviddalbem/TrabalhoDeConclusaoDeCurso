from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Orgao, TipoChamado
from Chamados.forms import CadastroTiposChamadosForm, AtualizarTiposChamadosForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def CadastroTipoChamado(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            pk = get_object_or_404(TipoChamado, id=pk)
        else:
            pk = None
        if request.method == 'POST':
            formEdit = CadastroTiposChamadosForm(request.POST, instance=pk)
            if formEdit.is_valid():
                formEdit.save()
                return redirect('Chamados:lista_tipo_chamado')
        else:
            formEdit = CadastroTiposChamadosForm(instance=pk)
            idOrgao = Orgao.objects.all()
            context = {'formEdit': formEdit,'idOrgao': idOrgao}
        return render(request, 'Chamados/cadastroTipoChamado.html', context)


@login_required
def tiposChamadosList(request):
    tipo_chamado_list = TipoChamado.objects.all()
    paginator = Paginator(tipo_chamado_list, 5)
    page = request.GET.get('page')
    tipo_chamado_list = paginator.get_page(page)
    context = {'tipo_chamado_list': tipo_chamado_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Chamados/listaTiposChamados.html', context)


class ListarTipoChamado(ListView):
    template_name = "Chamados/tiposChamadosList"
    context_object_name = 'lista_tipo_chamado'

    def get_queryset(self):
        self.id = get_object_or_404(TipoChamado, id=self.kwargs['pk'])
        return TipoChamado.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context

def atualizarTipoChamado(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            pk = get_object_or_404(TipoChamado, id=pk)
            print("aqui")
        else:
            pk = None

        if request.method == 'POST':
            formEdit = AtualizarTiposChamadosForm(request.POST, instance=pk)
            if formEdit.is_valid():
                formEdit.save()
                return redirect('Chamados:lista_tipo_chamado')
        else:
            formEdit = AtualizarTiposChamadosForm(instance=pk)
            idOrgao = Orgao.objects.all()
            context = {'formEdit': formEdit, 'idOrgao': idOrgao}
        return render(request, 'Chamados/atualizaTipoChamado.html', context)

class DeletarTipoChamado(DeleteView):
    model = TipoChamado
    template_name = "Chamados/tipo_Chamado_confirm_delete.html"
    success_url = reverse_lazy('Chamados:lista_tipo_chamado')

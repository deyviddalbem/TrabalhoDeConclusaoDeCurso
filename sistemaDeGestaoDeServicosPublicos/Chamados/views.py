from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Orgao, TipoChamado, Status, OcorrenciasChamado, Chamado, Endereco
from Chamados.forms import CadastroTiposChamadosForm, AtualizarTiposChamadosForm, CriarStatusForm, AtualizarStatusForm, CadastrarOcorrenciasChamadoForm, CriarChamadoForm
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
            context = {'formEdit': formEdit, 'idOrgao': idOrgao}
        return render(request, 'Chamados/tipoChamado/cadastroTipoChamado.html', context)


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
        return render(request, 'Chamados/tipoChamado/listaTiposChamados.html', context)


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
        return render(request, 'Chamados/tipoChamado/atualizaTipoChamado.html', context)


class DeletarTipoChamado(DeleteView):
    model = TipoChamado
    template_name = "Chamados/tipo_Chamado_confirm_delete.html"
    success_url = reverse_lazy('Chamados:lista_tipo_chamado')


class CadastrarStatus(CreateView):
    model = Status
    form_class = CriarStatusForm
    template_name = "Chamados/Status/cadastroStatus.html"
    success_url = reverse_lazy("Chamados:lista_status_chamado")


def ListaStatus(request):
    status_list = Status.objects.all()
    paginator = Paginator(status_list, 5)
    page = request.GET.get('page')
    status_list = paginator.get_page(page)
    context = {'status_list': status_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Chamados/Status/listarStatus.html', context)


class ListStatus(ListView):
    template_name = "Chamados/ListaStatus"
    context_object_name = 'status_list'

    def get_queryset(self):
        self.id = get_object_or_404(Status, id=self.kwargs['pk'])
        return Status.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context


def atualizarStatus(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            pk = get_object_or_404(Status, id=pk)
            print("aqui")
        else:
            pk = None

        if request.method == 'POST':
            formEdit = AtualizarStatusForm(request.POST, instance=pk)
            if formEdit.is_valid():
                formEdit.save()
                return redirect('Chamados:lista_status_chamado')
        else:
            formEdit = AtualizarStatusForm(instance=pk)
            context = {'formEdit': formEdit}
        return render(request, 'Chamados/Status/atualizarStatus.html', context)


class DeletarStatus(DeleteView):
    model = Status
    template_name = "Chamados/Status/status_confirm_delete.html"
    success_url = reverse_lazy('Chamados:lista_status_chamado')


class CadastrarOcorrencias(CreateView):
    model = OcorrenciasChamado
    form_class = CadastrarOcorrenciasChamadoForm
    template_name = "Chamados/Ocorrencias/cadastroOcorrenciaasChamado.html"
    success_url = reverse_lazy("Chamados:lista_status_chamado")


@login_required
def CadastroChamado(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            pk = get_object_or_404(Chamado, id=pk)
        else:
            pk = None
       
        if request.method == 'POST':
            formEdit = CriarChamadoForm(request.POST, instance=pk)
            if formEdit.is_valid():
                formEdit.save()
                return redirect('Chamados:lista_chamado')
            else:
                return HttpResponse("aqui")
        else:
            idStatus = Status.objects.filter(id=1)
            idOrgao = Orgao.objects.all()
            idTipoChamado = TipoChamado.objects.all()
            idUsuario = User.objects.filter(id=request.user.id)
            idEndereco = Endereco.objects.filter(idPessoa=request.user.id)
            formEdit = CriarChamadoForm(instance=pk)
            context = {'formEdit': formEdit, 'idOrgao': idOrgao, 'idTipoChamado': idTipoChamado, 'idStatus': idStatus,
                       'idUsuario': idUsuario, 'idEndereco': idEndereco}
            return render(request, 'Chamados/Chamados/criarChamado.html', context)
        


def ListaChamados(request):
    chamados_list = Chamado.objects.filter(idUsuario=request.user.id)
    paginator = Paginator(chamados_list, 5)
    page = request.GET.get('page')
    chamados_list = paginator.get_page(page)
    context = {'chamados_list': chamados_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Chamados/Chamados/listarChamado.html', context)


class ListChamados(ListView):
    template_name = "Chamados/ListaChamados"
    context_object_name = 'chamados_list'

    def get_queryset(self):
        self.id = get_object_or_404(Chamado, id=self.kwargs['pk'])
        return Chamado.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context

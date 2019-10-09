from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Orgao, TipoChamado, Status, OcorrenciasChamado, Chamado, Endereco
from Chamados.forms import CadastroTiposChamadosForm, AtualizarTiposChamadosForm, CriarStatusForm, AtualizarStatusForm, CadastrarOcorrenciasChamadoForm, CriarChamadoForm, AtualizarChamadoForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
def CadastroTipoChamado(request, pk=None):
    if not request.user.has_perm('TipoChamado.add_TipoChamado'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
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


def tiposChamadosList(request):
    if not request.user.has_perm('TiposChamados.view_TiposChamados'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        tipo_chamado_list = TipoChamado.objects.all()
        paginator = Paginator(tipo_chamado_list, 5)
        page = request.GET.get('page')
        tipo_chamado_list = paginator.get_page(page)
        context = {'tipo_chamado_list': tipo_chamado_list}
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            return render(request, 'Chamados/tipoChamado/listaTiposChamados.html', context)

def atualizarTipoChamado(request, pk=None):
    if not request.user.has_perm('TipoChamado.change_TipoChamado'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
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
    if not request.user.has_perm('Status.view_Status'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        status_list = Status.objects.all()
        paginator = Paginator(status_list, 5)
        page = request.GET.get('page')
        status_list = paginator.get_page(page)
        context = {'status_list': status_list}
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            return render(request, 'Chamados/Status/listarStatus.html', context)

def atualizarStatus(request, pk=None):
    if not request.user.has_perm('Status.add_Status'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
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
                if pk:
                    formEdit.save()
                else:
                    b = formEdit.save(commit=False)
                    b.numeroProtocolo = Chamado.gerarProtocolo()
                    print(Chamado.gerarProtocolo()+" aqui1122")
                    b.save()
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
    template_name = "Chamados/Chamados/listarChamado.html"
    context_object_name = 'chamados_list'
    paginate_by = 10000

    def get_queryset(self):
        self.id = get_object_or_404(Chamado, id=self.kwargs['pk'])
        return Chamado.objects.filter(idUsuario=self.request.user.id)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context

def detalheChamado(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            chamado = get_object_or_404(Chamado, id=pk)
            idStatus = Status.objects.filter(id=chamado.idStatus.id)
            idOrgao = Orgao.objects.all()
            idTipoChamado = TipoChamado.objects.filter(id=chamado.idTipoChamado.id)
            idUsuario = User.objects.filter(id=request.user.id)
            idEndereco = Endereco.objects.filter(idPessoa=request.user.id)
            nProtocolo = chamado.numeroProtocolo
            dataAbertura = chamado.dataAbertura
            dataConclusao = chamado.dataConclusao
            formEdit = AtualizarChamadoForm(instance=chamado)
            ocorrenciasChamado = OcorrenciasChamado.objects.filter(idChamado=pk)
            context = {'formEdit': formEdit, 'idOrgao': idOrgao, 'idTipoChamado': idTipoChamado, 'idStatus': idStatus,
                       'idUsuario': idUsuario, 'idEndereco': idEndereco, 'nProtocolo' : nProtocolo, 'dataAbertura':dataAbertura, 'dataConclusao': dataConclusao, 'ocorrenciasChamado': ocorrenciasChamado }
            return render(request, 'Chamados/Chamados/detalheChamado.html', context)
        else:
            chamado = None


def atualizarChamado(request, pk=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if pk:
            chamado = get_object_or_404(Chamado, id=pk)
        else:
            chamado = None

        if request.method == 'POST':
            formEdit = AtualizarChamadoForm(request.POST, instance=chamado)
            if formEdit.is_valid():
                formEdit.save()
                return redirect(reverse_lazy('Chamados:lista_chamado', kwargs={'pk':request.user.id}))

            else:
                return HttpResponse("deu pau")
        else:
            idStatus = Status.objects.all()
            idOrgao = Orgao.objects.all()
            idTipoChamado = TipoChamado.objects.filter(id=chamado.idTipoChamado.id)
            idUsuario = User.objects.filter(id=request.user.id)
            idEndereco = Endereco.objects.filter(idPessoa=request.user.id)
            nProtocolo = chamado.numeroProtocolo
            print (nProtocolo)
            formEdit = AtualizarChamadoForm(instance=chamado)
            context = {'formEdit': formEdit, 'idOrgao': idOrgao, 'idTipoChamado': idTipoChamado, 'idStatus': idStatus,
                       'idUsuario': idUsuario, 'idEndereco': idEndereco, 'nProtocolo' : nProtocolo }
        return render(request, 'Chamados/Chamados/atualizarChamado.html', context)


class FiltrarChamados(ListView):
    template_name = "Chamados/Chamados/listarChamado.html"
    context_object_name = 'chamados_list'
    paginate_by= 5

    def get_queryset(self):
        self.idPessoa = get_object_or_404(User, id=self.request.user.id)
        self.idStatus = get_object_or_404(
            Status, id=self.kwargs['statusChamado'])
        return Chamado.objects.filter(idUsuario_id=self.idPessoa, idStatus_id=self.idStatus)



def home_ajax_search(request, search_string=None):

    if search_string is None:
        chamados_list = Chamado.objects.filter(idUsuario = request.user.id)
    else:
        chamados_list = Chamado.objects.filter(numeroProtocolo__icontains=search_string) | Chamado.objects.filter(dataAbertura__icontains=search_string) | Chamado.objects.filter(idEndereco__logradouro__icontains=search_string) |  Chamado.objects.filter(idTipoChamado__descricaoTipoChamado__icontains=search_string)
        paginator = Paginator(chamados_list, 10)
        page = request.GET.get('page')
        chamados_list = paginator.get_page(page)
    return render(request, 'Chamados/Chamados/listarChamado.html', {'chamados_list': chamados_list})
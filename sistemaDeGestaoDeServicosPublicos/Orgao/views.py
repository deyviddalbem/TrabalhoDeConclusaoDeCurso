from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao, TipoLotacao
from Orgao.forms import CadastroOrgaoForm, CadastroTipoLotacaoForm, CadastroLotacaoForm, AtualizarLotacaoForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User


# Create your views here.


def indexOrgao(request):
    idOrgao = request.session['idVinculo']
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        orgaoSelecionado = get_object_or_404(Orgao, pk=idOrgao)
        context = {'orgaoSelecionado':  orgaoSelecionado}
        return render(request, 'Orgao/index.html', context)


def retornaLotacao(request):
    lotacao = Lotacao.objects.filter(idUsuario=request.user.id)
    context = {'userServidor': lotacao}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        if request.method == 'POST':
            idOrgaoVinculo = request.POST.get('idOrgao')
            orgaoVinculo = get_object_or_404(Orgao, pk=idOrgaoVinculo)
            request.session['idVinculo'] = idOrgaoVinculo
            request.session['nomeVinculo'] = orgaoVinculo.nomeOrgao
            return redirect('Orgao:orgao_index')

        else:
            if len(lotacao) == 0:
                return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html', context)
            else:
                request.session['temVinculo'] = 'yes'
                return render(request, 'Orgao/escolheVinculo.html', context)
        return HttpResponse(request.POST.get('idOrgao'))


def orgaoList(request):
    orgao_list = Orgao.objects.all()
    context = {'orgao_list': orgao_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Orgao/dadosOrgao.html', context)


class ListarOrgao(ListView):
    template_name = "Orgao/orgaoList"
    context_object_name = 'orgao_list'

    def get_queryset(self):
        self.id = get_object_or_404(Orgao, id=self.kwargs['pk'])
        return Orgao.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context


def TipoLotacaoList(request):
    tipo_lotacao_list = TipoLotacao.objects.all()
    paginator = Paginator(tipo_lotacao_list, 5)
    page = request.GET.get('page')
    tipo_lotacao_list = paginator.get_page(page)
    context = {'tipo_lotacao_list': tipo_lotacao_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Orgao/tiposLotacao.html', context)


class ListarTipoLotacao(ListView):
    template_name = "Orgao/TipoLotacaoList.html"
    context_object_name = 'tipo_lotacao'

    def get_queryset(self):
        self.id = get_object_or_404(TipoLotacao, id=self.kwargs['pk'])
        return TipoLotacao.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context


class CriarOrgao(CreateView):
    model = Orgao
    form_class = CadastroOrgaoForm
    template_name = "Orgao/cadastroOrgao.html"
    success_url = reverse_lazy("Orgao:orgao_index")


class AtualizarOrgao(UpdateView):
    model = Orgao
    form_class = CadastroOrgaoForm
    template_name = "Orgao/atualizarOrgao.html"
    success_url = reverse_lazy('Orgao:dados_orgao')


class CadastrarTipoLotacao(CreateView):
    model = TipoLotacao
    form_class = CadastroTipoLotacaoForm
    template_name = "Orgao/cadastroTipoLotacao.html"
    success_url = reverse_lazy("Orgao:tipos_lotacao")


class AtualizarTipoLotacao(UpdateView):
    model = TipoLotacao
    form_class = CadastroTipoLotacaoForm
    template_name = "Orgao/atualizarTipoLotacao.html"
    success_url = reverse_lazy('Orgao:tipos_lotacao')


class DeletarTipoLotacao(DeleteView):
    model = TipoLotacao
    template_name = "Orgao/tipoLotacao_Confirm_delete.html"
    success_url = reverse_lazy('Orgao:tipos_lotacao')


def CadastroLotacao(request, idL=None):
    if idL:
        idL = get_object_or_404(Lotacao, id=idL)
    else:
        idL = None

        formEdit = CadastroLotacaoForm(request.POST, instance=idL)
    if request.method == 'POST':

        if formEdit.is_valid():
            formEdit.save()
            return redirect('Orgao:tipos_lotacao')
    else:
        tipoLotacao = TipoLotacao.objects.all()
        idUsuario = User.objects.all()
        idOrgao = Orgao.objects.all()
        context = {'formEdit': formEdit, 'tipoLotacao': tipoLotacao,
                   'idUsuario': idUsuario, 'idOrgao': idOrgao}
    return render(request, 'Orgao/cadastroLotacao.html', context)


def LotacaoList(request):
    lotacao_list = Lotacao.objects.all()
    paginator = Paginator(lotacao_list, 6)
    page = request.GET.get('page')
    lotacao_list = paginator.get_page(page)
    context = {'lotacao_list': lotacao_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Orgao/lotacaoList.html', context)


class ListarLotacao(ListView):
    template_name = "Orgao/LotacaoList.html"
    context_object_name = 'list_lotacao'

    def get_queryset(self):
        self.id = get_object_or_404(Lotacao, id=self.kwargs['pk'])
        return Lotacao.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['id'] = self.id
        return context


class AtualizarLotacao(UpdateView):
    model = Lotacao
    form_class = AtualizarLotacaoForm
    template_name = "Orgao/atualizarLotacao.html"
    success_url = reverse_lazy('Orgao:lista_lotacao')


def atualiza_Lotacao(request, idLotacao=None):
    tipoLotacao = TipoLotacao.objects.all()
    idUsuario = User.objects.all()
    idOrgao = Orgao.objects.all()
    if idLotacao:
        idLotacao = get_object_or_404(Lotacao, id=idLotacao)
        print("aqui")
    else:
        idLotacao = None
        

   
    if request.method == 'POST':
        formEdit = AtualizarLotacaoForm(request.POST, instance=idLotacao)
        if formEdit.is_valid():
            formEdit.save()
            return redirect('Orgao:lista_lotacao')
    else:
        formEdit= AtualizarLotacaoForm(instance=idLotacao)
        context = {'formEdit': formEdit, 'tipoLotacao': tipoLotacao,
                   'idUsuario': idUsuario, 'idOrgao': idOrgao}
    return render(request, 'Orgao/atualizarLotacao.html', context)

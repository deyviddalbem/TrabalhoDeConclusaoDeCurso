import json
from social_django.models import UserSocialAuth
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao, TipoLotacao
from Orgao.forms import CadastroOrgaoForm, CadastroTipoLotacaoForm, CadastroLotacaoForm, AtualizarLotacaoForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied


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
    context= {}
    try:
        picture = UserSocialAuth.objects.get(uid=request.user.email)
        path_dump = json.dumps(picture.extra_data)
        path_load = json.loads(path_dump)
        picture = path_load["picture"]
        context = {'picture': picture}
        request.session['profile_picture'] = picture
    except:
        pass
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
                return HttpResponseRedirect(reverse('index'))
            else:
                request.session['temVinculo'] = 'yes'
                return render(request, 'Orgao/escolheVinculo.html', context)
        return HttpResponse(request.POST.get('idOrgao'))


class CriarOrgao(CreateView):
    model = Orgao
    form_class = CadastroOrgaoForm
    template_name = "Orgao/cadastroOrgao.html"
    success_url = reverse_lazy("Orgao:orgao_index")


def orgaoList(request):
    if not request.user.has_perm('Orgao.view_Orgao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else: 
        orgao_list = Orgao.objects.all()
        context = {'orgao_list': orgao_list}
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            return render(request, 'Orgao/dadosOrgao.html', context)


def atualizaOrgao(request, idOrgao=None):
    if not request.user.has_perm('Orgao.change_Orgao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            if idOrgao:
                idOrgao = get_object_or_404(Orgao, id=idOrgao)
                print("aqui")
            else:
                idOrgao = None
            if request.method == 'POST':
                formEdit = CadastroOrgaoForm(request.POST, instance=idOrgao)
                if formEdit.is_valid():
                    formEdit.save()
                    return redirect('Orgao:dados_orgao')
            else:
                formEdit = CadastroOrgaoForm(instance=idOrgao)
                context = {'formEdit': formEdit}
            return render(request, 'Orgao/atualizarOrgao.html', context)


class CadastrarTipoLotacao(CreateView):
    model = TipoLotacao
    form_class = CadastroTipoLotacaoForm
    template_name = "TipoLotacao/cadastroTipoLotacao.html"
    success_url = reverse_lazy("Orgao:tipos_lotacao")


def TipoLotacaoList(request):
    if not request.user.has_perm('TipoLotacao.view_TipoLotacao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            tipo_lotacao_list = TipoLotacao.objects.all()
            paginator = Paginator(tipo_lotacao_list, 5)
            page = request.GET.get('page')
            tipo_lotacao_list = paginator.get_page(page)
            context = {'tipo_lotacao_list': tipo_lotacao_list}
            if not request.user.is_authenticated:
                return render(request, 'Usuario/acessoNegado.html')
            else:
                return render(request, 'TipoLotacao/tiposLotacao.html', context)


class AtualizarTipoLotacao(UpdateView):
    model = TipoLotacao
    form_class = CadastroTipoLotacaoForm
    template_name = "TipoLotacao/atualizarTipoLotacao.html"
    success_url = reverse_lazy('Orgao:tipos_lotacao')


class DeletarTipoLotacao(DeleteView):
    model = TipoLotacao
    template_name = "TipoLotacao/tipoLotacao_Confirm_delete.html"
    success_url = reverse_lazy('Orgao:tipos_lotacao')


def CadastroLotacao(request, idL=None):
    if not request.user.has_perm('Lotacao.add_Lotacao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            if idL:
                idL = get_object_or_404(Lotacao, id=idL)
            else:
                idL = None

                formEdit = CadastroLotacaoForm(request.POST, instance=idL)
            if request.method == 'POST':

                if formEdit.is_valid():
                    usuario = User.objects.get(id=request.POST.get('idUsuario'))
                    tipo_Lotacao =TipoLotacao.objects.get(id = request.POST.get('idTipoLotacao'))
                    grupo = Group.objects.get(name= tipo_Lotacao.descricao)
                    usuario.groups.add(grupo)
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
    if not request.user.has_perm('Lotacao.add_Lotacao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
            lotacao_list = Lotacao.objects.all()
            paginator = Paginator(lotacao_list, 6)
            page = request.GET.get('page')
            lotacao_list = paginator.get_page(page)
            context = {'lotacao_list': lotacao_list}
            if not request.user.is_authenticated:
                return render(request, 'Usuario/acessoNegado.html')
            else:
                return render(request, 'Lotacao/lotacaoList.html', context)

def atualiza_Lotacao(request, idLotacao=None):
    if not request.user.has_perm('Lotacao.add_Lotacao'):
        return render(request, 'Orgao/bloqueioDeAcesso.html')
    else:
        if not request.user.is_authenticated:
            return render(request, 'Usuario/acessoNegado.html')
        else:
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
                formEdit = AtualizarLotacaoForm(instance=idLotacao)
                context = {'formEdit': formEdit, 'tipoLotacao': tipoLotacao,
                        'idUsuario': idUsuario, 'idOrgao': idOrgao}
            return render(request, 'Lotacao/atualizarLotacao.html', context)


class DeletarLotacao(DeleteView):
    model = Lotacao
    template_name = "Lotacao/lotacao_confirm_delete.html"
    success_url = reverse_lazy('Orgao:lista_lotacao')

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao
from Orgao.forms import CadastroOrgaoForm

# Create your views here.

def indexOrgao(request):
    idOrgao = request.GET.get('idOrgao')
    if idOrgao == None:
        context = {'orgaoSelecionado':  idOrgao}
        return render(request, 'Orgao/index.html', context)
    else:
        return HttpResponse("aqui")


def retornaLotacao(request):    
    lotacao = Lotacao.objects.filter(idUsuario=request.user.id)
    context = {'userServidor': lotacao}
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
    orgao_list = Orgao.objects.filter(id=1)
    context = {'orgao_list': orgao_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Orgao/dadosOrgao.html', context)


class CriarOrgao(CreateView):
    model = Orgao
    form_class = CadastroOrgaoForm
    template_name = "Orgao/cadastroOrgao.html"
    success_url = reverse_lazy("Orgao:orgao_index")
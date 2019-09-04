from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Lotacao, Orgao


# Create your views here.

def indexOrgao(request):
    if not request.user.is_authenticated:
        return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html')
    else:
        return render(request, 'Orgao/indexOrgaoGerenteGeral.html')



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

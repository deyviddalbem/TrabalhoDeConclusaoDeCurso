from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import PessoaUserForm, CadastroTelefoneForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Telefone, TipoTelefone


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html')
    else:
        return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html')


class CriarCadastro(CreateView):
    model = User
    form_class = PessoaUserForm
    template_name = "Usuario/cadastroUsuario.html"
    success_url = reverse_lazy('login')


def enderecosList(request):
    # enderecos_list = Endereco.objects.filter(idPessoa_id=request.user.id)
    # context = {'enderecos_list': enderecos_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Usuario/enderecosList.html')


def CadastroTelefone(request, idTelefone=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        tipos = TipoTelefone.objects.all()
        if idTelefone:
            meuTelefone = get_object_or_404(Telefone, id=idTelefone)
        else:
            meuTelefone = None

        if request.method == 'POST':
            formEdit = CadastroTelefoneForm(request.POST, instance=meuTelefone)
            if formEdit.is_valid():
                formEdit.save()
                return redirect('listaTelefones')
        else:
            formEdit = meuTelefone
            context = {'formEdit': formEdit, 'tipos': tipos}
        return render(request, 'Usuario/cadastroTelefone.html', context)


def TelefonesList(request):
    telefones_list = Telefone.objects.filter(idPessoa_id=request.user.id)
    context = {'telefones_list': telefones_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Usuario/telefonesList.html', context)

def atualizarMeusTelefones(request, idTelefone=None):
    
    tipos = TipoTelefone.objects.all()
    if idTelefone:
        meuTelefone = get_object_or_404(Telefone, id=idTelefone)
    else:
        meuTelefone = None

    if request.method == 'POST':
        formEdit = CadastroTelefoneForm(request.POST, instance=meuTelefone)
        if formEdit.is_valid():
            formEdit.save()
            return redirect('listaTelefones')
    else:
        formEdit = meuTelefone
        context = {'formEdit': formEdit, 'tipos': tipos}
    return render(request, 'Usuario/atualizarTelefones.html', context)

class DeletarTelefone(DeleteView):
    model = Telefone
    template_name = "Usuario/telefone_confirm_delete.html"
    success_url = reverse_lazy('listaTelefones')



def CadastroEndereco(request, idTelefone=None):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Usuario/enderecosList.html')

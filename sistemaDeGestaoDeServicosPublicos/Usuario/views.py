from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import PessoaUserForm, CadastroTelefoneForm, CadastroEnderecoForm, PessoaUserFormUpdate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Telefone, TipoTelefone, Endereco


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

class AtualizarCadastro(UpdateView):
    model = User
    form_class = PessoaUserFormUpdate
    template_name = "Usuario/atualizarCadastro.html"
    success_url = reverse_lazy('index')

class CriarEndereco(CreateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "Usuario/cadastroEndereco.html"
    success_url = reverse_lazy('login')

def enderecosList(request):
    enderecos_list = Endereco.objects.filter(idPessoa_id=request.user.id)
    context = {'enderecos_list': enderecos_list}
    return render(request, 'Usuario/enderecosList.html', context)


def CadastroTelefone(request, idTelefone=None):
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


def mostrarMeusDados(request):
    dadosUserList = User.objects.filter(id=request.user.id)
    context = {'dadosUserList': dadosUserList}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Usuario/meusDados.html', context)


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


def cadastroEndereco(request,idEndereco=None):
    if idEndereco:
        meuEndereco = get_object_or_404(Endereco, id=idEndereco)
    else:
        meuEndereco = None

    if request.method == 'POST':
        formEdit = CadastroEnderecoForm(request.POST, instance=meuEndereco)
        if formEdit.is_valid():
            formEdit.save()
            return redirect('enderecosList')
    else:
        formEdit = meuEndereco
        context = {'formEdit': formEdit }
    return render(request, 'Usuario/cadastroEndereco.html', context)

def enderecosList(request):
    enderecos_list = Endereco.objects.filter(idPessoa_id=request.user.id)
    context = {'enderecos_list': enderecos_list}
    return render(request, 'Usuario/enderecosList.html', context)

class ListarEnderecos(ListView):
    template_name = "Usuario/enderecosList.html"
    context_object_name = 'enderecos_list'

    def get_queryset(self):
        self.idPessoa = get_object_or_404(User, id=self.kwargs['pk'])
        return Endereco.objects.filter(idPessoa_id=self.idPessoa)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['idPessoa'] = self.idPessoa
        return context


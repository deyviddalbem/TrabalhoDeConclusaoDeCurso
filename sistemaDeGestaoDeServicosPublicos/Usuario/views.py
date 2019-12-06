import json
from social_django.models import UserSocialAuth
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
    if not request.user.is_authenticated:
        return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html')
    else:
        return render(request, 'sistemaDeGestaoDeServicosPublicos/index1.html')

##### Função para criar a view de cadastro de usuário ######
class CriarCadastro(CreateView):
    model = User
    form_class = PessoaUserForm
    template_name = "Usuario/cadastroUsuario.html"
    success_url = reverse_lazy('login')

class AtualizarCadastro(UpdateView):
    model = User
    form_class = PessoaUserFormUpdate
    template_name = "Usuario/atualizarCadastro.html"
    success_url = reverse_lazy('meusDados')

def mostrarMeusDados(request):
    dadosUserList = User.objects.filter(id=request.user.id)
    context = {'dadosUserList': dadosUserList}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Usuario/meusDados.html', context)



##### Função para efetuar o cadastro do telefone #####
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
    return render(request, 'Telefone/cadastroTelefone.html', context)

##### Função para lstar os telefones #####
def TelefonesList(request):
    telefones_list = Telefone.objects.filter(idPessoa_id=request.user.id)
    context = {'telefones_list': telefones_list}
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        return render(request, 'Telefone/telefonesList.html', context)


##### Função para atualizar os telefones #####
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
    return render(request, 'Telefone/atualizarTelefones.html', context)

##### Função para excluir os telefones #####
class DeletarTelefone(DeleteView):
    model = Telefone
    template_name = "Telefone/telefone_confirm_delete.html"
    success_url = reverse_lazy('listaTelefones')

##### Função que efetua o cadastro de endereço #####
def cadastroEndereco(request):
    if request.method == 'POST':
        address_form = CadastroEnderecoForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            return redirect('listaEnderecos')
        else:
            context = {'address_form': address_form}
            return render(request, 'Endereco/cadastroEndereco.html', context)

    else:
        address_form = CadastroEnderecoForm()
        context = {'address_form': address_form}
        return render(request, 'Endereco/cadastroEndereco.html', context)


##### Função que lista os enderecos #####
def enderecosList(request):
    if not request.user.is_authenticated:
        return render(request, 'Usuario/acessoNegado.html')
    else:
        enderecos_list = Endereco.objects.filter(idPessoa_id=request.user.id)
        context = {'enderecos_list': enderecos_list}
        return render(request, 'Endereco/enderecosList.html', context)

class ListarEnderecos(ListView):
    template_name = "Endereco/enderecosList.html"
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

##### função que efetua a atualização do endereco #####
class AtualizarEndereco(UpdateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "Endereco/atualizarEndereco.html"
    success_url = reverse_lazy('listaEnderecos')

##### Função que efetua a exclusão do endereco #####
class DeletarEndereco(DeleteView):
    model = Endereco
    template_name = "Endereco/endereco_confirm_delete.html"
    success_url = reverse_lazy('listaEnderecos')

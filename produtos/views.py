from django.shortcuts import render
from .models import Produto
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm

from .serializers import ProdutoSerializer
from rest_framework import viewsets, permissions

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.AllowAny]


def formlogin(request):

    if request.method == "POST":
        usuario = request.POST['login']
        senha = request.POST['senha']        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/produtos/listarprodutos")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/produtos/login")

@login_required(login_url="/produtos/login")
def listarProdutos(request):
    busca = request.GET.get('busca', '').strip()

    if busca:
        produtos = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos = Produto.objects.all()

    return render(request, "listarProdutos.html", {
        "produtos": produtos
    })

@login_required(login_url="/produtos/login")
def cadastroProduto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produtos/listarprodutos')
    else:
        form = ProdutoForm() 

    return render(request, "cadastroProduto.html", {'form': form})

@login_required(login_url="/produtos/login")
def excluirProduto(request, id):

    produto = Produto.objects.get(id=id)
    produto.delete()

    return HttpResponseRedirect('/produtos/listarprodutos')

@login_required(login_url="/produtos/login")
def editarProduto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/produtos/listarprodutos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, "editarProduto.html", {'form': form})


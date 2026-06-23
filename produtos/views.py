from django.shortcuts import render
from .models import Produto
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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

    if request.method == "GET" and request.GET.get('busca'):
        produtos = Produto.objects.filter(nome__icontains=request.GET.get('busca'))
    else:
        produtos = Produto.objects.all()

    return render(request, "listarProdutos.html", {"produtos" : produtos})

@login_required(login_url="/produtos/login")
def cadastroProduto(request):

    if(request.method == "POST"):
        nome = request.POST.get('nome')      
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')

        novo_produto = Produto(nome=nome, 
                                categoria=categoria, 
                                preco=preco, 
                                )
        novo_produto.save()

        return HttpResponseRedirect('/produtos/listarprodutos')

    produtos = Produto.objects.all()

    return render(request, "cadastroProduto.html", {'produtos':produtos})

@login_required(login_url="/produtos/login")
def excluirProduto(request, id):

    produto = Produto.objects.get(id=id)
    produto.delete()

    return HttpResponseRedirect('/produtos/listarprodutos')

@login_required(login_url="/produtos/login")
def editarProduto(request, id):

    if request.method == "POST":
        nome = request.POST.get('nome')      
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')

        editar_produto = Produto.objects.get(id=id)
        editar_produto.nome = nome
        editar_produto.categoria = categoria
        editar_produto.preco = preco
       
        editar_produto.save()

        return HttpResponseRedirect('/produtos/listarprodutos')
    else:
        produto = Produto.objects.get(id=id)
        

    return render(request, "editarProduto.html",{'produto': produto})



from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import Produto, Cliente, Carrinho, Lista_desejos
from .forms import RegistroClienteForm, ClientePerfilForm
from django.contrib import messages
from django.db.models import Q
from django.conf import settings

# Views referentes aos produtos do ecommerce

def home(request):
    return render(request, 'produto/home.html')


def sobre(request):
    return render(request, 'produto/sobre.html')


class CategoriaView(View):
    def get(self, request, val):
        if 'q' in request.GET:
            q = request.GET['q']
            produto = Produto.objects.filter(Q(nome_produto__icontains=q) & Q(categoria_produto = val))
        else:
            produto = Produto.objects.filter(categoria_produto=val)
        return render(request, 'produto/categoria.html', locals())


class InformacoesProdutoView(View):
    def get(self, request, pk):
        produto = Produto.objects.get(pk=pk)
        produto_no_carrinho = Carrinho.objects.filter(Q(produto=produto) & Q(usuario=request.user))
        lista_desejos = Lista_desejos.objects.filter(Q(produto=produto) & Q(usuario=request.user))
        return render(request, 'produto/informacoes_produto.html', locals())


def add_ao_carrinho(request):
    user = request.user
    produto_id = request.GET.get('prod_id')
    produto = Produto.objects.get(id=produto_id)
    Carrinho(usuario=user, produto=produto).save()
    return redirect('/carrinho')


def mostrar_carrinho(request):
    user = request.user
    carrinho = Carrinho.objects.filter(usuario=user)
    total = 0
    for p in carrinho:
        value = p.quantidade * p.produto.preco_desconto
        total = total + value
    total_tudo = total + 40
    return render(request, 'produto/add_ao_carrinho.html', locals())


def add_lista_desejos(request):
    user = request.user
    produto_id = request.GET.get('prod_id')
    produto = Produto.objects.get(id=produto_id)
    Lista_desejos(usuario=user, produto=produto).save()
    return redirect('/lista_desejos')


def mostrar_lista_desejos(request):
    user = request.user
    lista_desejos = Lista_desejos.objects.filter(usuario=user)
    return render(request, 'produto/add_lista_desejos.html', locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carrinho.objects.get(Q(produto=prod_id) & Q(usuario=request.user))
        c.quantidade += 1
        c.save()
        usuario = request.user
        carrinho = Carrinho.objects.filter(usuario=usuario)
        total = 0
        for p in carrinho:
            valor = p.quantidade * p.produto.preco_desconto
            total = total + valor
        total_tudo = total + 40
        data = {
            'quantidade': c.quantidade,
            'total': total,
            'total_tudo': total_tudo
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carrinho.objects.get(Q(produto=prod_id) & Q(usuario=request.user))
        c.quantidade -= 1
        c.save()
        usuario = request.user
        carrinho = Carrinho.objects.filter(usuario=usuario)
        total = 0
        for p in carrinho:
            valor = p.quantidade * p.produto.preco_desconto
            total = total + valor
        total_tudo = total + 40
        data = {
            'quantidade': c.quantidade,
            'total': total,
            'total_tudo': total_tudo
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carrinho.objects.get(Q(produto=prod_id) & Q(usuario=request.user))
        c.delete()
        usuario = request.user
        carrinho = Carrinho.objects.filter(usuario=usuario)
        total = 0
        for p in carrinho:
            valor = p.quantidade * p.produto.preco_desconto
            total = total + valor
        total_tudo = total + 40
        data = {
            'total': total,
            'total_tudo': total_tudo
        }
        return JsonResponse(data)


def remove_desejo(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Lista_desejos.objects.get(Q(produto=prod_id) & Q(usuario=request.user))
        c.delete()
        return JsonResponse(data)


 #Views referentes ao cliente e autenticações
class RegistroClienteView(View):
    def get(self, request):
        form = RegistroClienteForm()
        return render(request, 'usuario/registro_conta_cliente.html', locals())

    def post(self, request):
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parabéns! Você acabou de criar uma conta!")
        else:
            messages.warning(request, "Ops! Os dados estão inválidos.")
        return render(request, 'usuario/registro_conta_cliente.html', locals())


class ProfileView(View):
    def get(self, request):
        form = ClientePerfilForm()
        return render(request, 'usuario/profile.html', locals())

    def post(self, request):
        form = ClientePerfilForm(request.POST)
        if form.is_valid():
            user = request.user
            nome = form.cleaned_data['nome']
            localidade = form.cleaned_data['localidade']
            cidade = form.cleaned_data['cidade']
            telemovel = form.cleaned_data['telemovel']
            estado = form.cleaned_data['estado']
            cep = form.cleaned_data['cep']

            registro = Cliente(usuario=user, nome=nome, localidade=localidade, cidade=cidade, telemovel=telemovel,
                               estado=estado, cep=cep)
            registro.save()
            messages.success(request, 'Parabéns! Você registrou os dados de sua conta com sucesso!')
        else:
            messages.warning(request, 'Os dados estão invalidos!')
        return render(request, 'usuario/profile.html', locals())


def endereco(request):
    user = request.user
    add = Cliente.objects.filter(usuario=user)
    return render(request, 'usuario/endereco.html', locals())


class AtualizarEndereco(View):
    def get(self, request, pk):
        add = Cliente.objects.get(pk=pk)
        form = ClientePerfilForm(instance=add)
        return render(request, 'usuario/atualizar_endereco.html', locals())

    def post(self, request, pk):
        form = ClientePerfilForm(request.POST)
        if form.is_valid():
            update = Cliente.objects.get(pk=pk)
            update.nome = form.cleaned_data['nome']
            update.localidade = form.cleaned_data['localidade']
            update.cidade = form.cleaned_data['cidade']
            update.telemovel = form.cleaned_data['telemovel']
            update.estado = form.cleaned_data['estado']
            update.cep = form.cleaned_data['cep']
            update.save()
            messages.success(request, 'Você alterou os dados com sucesso!')
        else:
            messages.warning(request, 'Os dados foram enviados de forma inválida!')
        return redirect("endereco")

from django.contrib import admin
from .models import  Produto, Cliente, Carrinho,Lista_desejos

@admin.register(Produto)
class ProdutoAdminModel(admin.ModelAdmin):
    list_display = ['id','nome_produto','preco_venda','preco_desconto']

@admin.register(Cliente)
class ClienteAdminModel(admin.ModelAdmin):
    list_display = ['id','usuario','nome','cidade','estado']

@admin.register(Carrinho)
class CarrinhoModelAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','produto','quantidade']


@admin.register(Lista_desejos)
class Lista_desejos_admin(admin.ModelAdmin):
    list_display = ['id','usuario','produto']
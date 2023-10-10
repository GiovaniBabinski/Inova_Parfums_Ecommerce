from django.db import models
from django.contrib.auth.models import User

CATEGORIA_CHOICES = (
    ('PF', 'Perfumes'),
    ('DE', 'Desodorantes'),
    ('LO', 'Locoes'),
    ('SH', 'Shampoos'),
    ('CO', 'Condicionadores'),
    ('CR', 'Cremes'),
    ('SA', 'Sabonetes'),
    ('ES', 'Esmaltes'),
    ('MA', 'Maquiagens'),
)

ESTADO_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amapa'),
    ('AZ', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceara'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goias'),
    ('MA', 'Maranhao'),
    ('MT', 'Mato Grosso'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Para'),
    ('PB', 'Paraiba'),
    ('PR', 'Parana'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piaui'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondonia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'Sao Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

CONSUMIDOR_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('U', 'Unissex')
)


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    foto_produto = models.ImageField(upload_to='product')
    descricao_produto = models.TextField(max_length=650)
    consumidor = models.CharField(choices=CONSUMIDOR_CHOICES, max_length=2, default='M')
    categoria_produto = models.CharField(choices=CATEGORIA_CHOICES, max_length=2)
    preco_venda = models.FloatField()
    preco_desconto = models.FloatField()
    composicao = models.CharField(max_length=350)

    def __str__(self):
        return self.nome_produto


class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    localidade = models.CharField(max_length=200)
    cidade = models.CharField(max_length=50)
    telemovel = models.IntegerField(default=0)
    cep = models.IntegerField()
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=100)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantidade * self.produto.preco_desconto


class Lista_desejos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

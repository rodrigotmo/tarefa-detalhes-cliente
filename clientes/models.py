from django.db import models
from django.contrib import admin

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=35)
    cidade = models.CharField(max_length=35)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.rua

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    genero = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=20)
    telefone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    data_cadastro = models.DateTimeField()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    @admin.display()
    def cidade(self):
        return self.endereco.cidade
from django.contrib import admin
from .models import Endereco, Cliente

# Register your models here.

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cidade', 'data_cadastro')
    search_fields = ('nome', 'sobrenome')
    list_per_page = 10
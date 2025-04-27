from django.shortcuts import render
from .models import Cliente, Endereco

# Create your views here.

def index(request):
    lista_clientes = Cliente.objects.all()
    dados = {
        'clientes': lista_clientes,
    }
    return render(request, 'clientes/index.html', dados)

def cliente_detalhes(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    dados = {
        'cliente': cliente
    }
    return render(request, 'clientes/cliente_detalhes.html', dados)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/<id_cliente>', views.cliente_detalhes, name='url_cliente_detalhes')
]
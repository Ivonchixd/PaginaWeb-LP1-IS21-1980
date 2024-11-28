from django.shortcuts import render
from .models import products
# Create your views here.
from django.http import HttpResponse
from django.urls import path
from django.template import loader

def Productos(request):
    #return HttpResponse("Estos son los productos (Mi primera vista)")
    misProductos = products.objects.all().values()
    template = loader.get_template("bProductos.html")
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

def ProductoDetalle(request, codigoProducto):
    miProducto = products.objects.get(codigoProducto=codigoProducto)
    template = loader.get_template('productoDetalle.html')
    context = {
        'miProducto': miProducto,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    return render(request, 'index.html')
from django.shortcuts import render


def shippingCrud(request):
    return render(request, 'envio_modifi.html')

def index(request):
    return render(request, 'index.html')

def newShipping(request):

    return render(request, 'nuevo_envio.html')

def trazabilidad(request):
    return render(request, 'trazabilidad.html')

def userCrud(request):
    return render(request, 'usuarios.html')
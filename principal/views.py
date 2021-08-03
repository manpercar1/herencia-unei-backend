from django.http.response import JsonResponse
from principal import models
from numpy import random

# Create your views here.
def findAllSolicitudes(request):

    return JsonResponse(models.data(), safe=False)

def numeroRandom(request):
    x = random.rand()
    context = {
            'numero' : x
        }
    return JsonResponse(context, safe=False)

def obtenerCliente(request, posicionCliente):
    clientes = models.dataHerencia()
    clienteSeleccionado = {}
    for cliente in clientes:
        if cliente['expediente']['codExpedienteUNEI'] == str(posicionCliente):
            clienteSeleccionado.update(cliente)
    return JsonResponse(clienteSeleccionado, safe=False)

def obtenerClientes(request, tenant):
    clientes = models.dataHerencia()
    clientesTenant = []
    for cliente in clientes:
        if cliente['expediente']['idTenant'] == tenant:
            clientesTenant.append(cliente)
    # context = {
    #     "numero resultados" : len(clientesTenant),
    #     "clientes" : clientesTenant
    # }

    # return JsonResponse(context, safe=False)
    return JsonResponse(clientesTenant, safe=False)

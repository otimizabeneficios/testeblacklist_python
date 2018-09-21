from django.http import HttpResponse
from cpfhandler import CpfHandler

def consulta(request, cpfConsulta):

    if(not CpfHandler.validarCpf(cpfConsulta)):
        resposta = 'RUNNING'
    else:

        cpf = CpfHandler.converterCpf(cpfConsulta)

        if(CpfHandler.checarBlacklist(cpf)):
            resposta = 'BLOCK'
        else:
            resposta = 'FREE'

    return HttpResponse(resposta)

def index(request):
    return HttpResponse('Vitor Nascimento')
from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Pront para investir!')

def novo_investimento(request):
    return render(request,'intestimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('Tipoinvestimento')
    }
    return render(request,'investimentos/investimento_registrado.html',investimento)
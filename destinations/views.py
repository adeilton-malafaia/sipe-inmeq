from django.shortcuts import render


def home(request):
    return render(request, 'destinations/pages/index.html')


def entidades(request):  # View de rota para cadastro de entidades
    return render(request, 'destinations/pages/cadastro-entidade.html')


def destino(request):  # View de rota para registro de destino de produtos
    return render(request, 'destinations/pages/registro-destino.html')


def doacao(request):  # View de rota para registro de doação
    return render(request, 'destinations/pages/registro-doacao.html')


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, 'destinations/pages/gerar-planilha.html')

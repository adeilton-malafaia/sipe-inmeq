from django.shortcuts import render


def entidades(request):  # View de rota para cadastro de entidades
    return render(request, 'destino_produtos/pages/cadastro-entidades.html')


def destino(request):  # View de rota para registro de destino de produtos
    return render(request, 'destino_produtos/pages/registro-destino.html')


def doacao(request):  # View de rota para registro de doação
    return render(request, 'destino_produtos/pages/registro-doacao.html')


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, 'destino_produtos/pages/gerar-planilha.html')

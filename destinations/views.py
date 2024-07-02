from django.shortcuts import render

from utils.destinations.factory import makeSaida

from . import forms, models


def home(request):
    return render(request, 'destinations/pages/index.html')


def entidades(request):  # View de rota para cadastro de entidades
    entidades = models.Entidade.objects.all().order_by('rs').filter(ativo='s')
    return render(request,
                  'destinations/pages/cadastro-entidade.html',
                  context={'entidades': entidades})


def cadentidades(request):  # View de rota para cadastro de entidades
    if request.POST:
        POST = request.POST
        request.session['register_form_entidades'] = POST
        form = forms.EntidadeForm(POST)
    else:
        form = forms.EntidadeForm()
    return render(request,
                  'destinations/pages/entidades.html',
                  {'form': form, }
                  )


def saidas(request):  # View de rota para registro de destino de produtos
    return render(request,
                  'destinations/pages/registro-saidas.html',
                  context={
                      'saidas': [makeSaida() for _ in range(30)]
                  })


def registrodestino(request):  # View de rota para registro de doação
    return render(request, 'destinations/pages/registro-destino.html')


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, 'destinations/pages/gerar-planilha.html')

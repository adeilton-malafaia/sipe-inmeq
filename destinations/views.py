from django.contrib import messages
from django.shortcuts import render

from utils.destinations.factory import makeSaida

from . import forms


def home(request):
    return render(request, "destinations/pages/index.html")


def entidades(request):  # View de rota para cadastro de entidades
    if request.POST:
        POST = request.POST
        request.session["register_form_entidades"] = POST
        form = forms.EntidadeForm(POST)
        if form.is_valid():
            print(POST)
            form.save(commit=True)
            messages.success(request, "ENTIDADE SALVA COM SUCESSO")
            del request.session["register_form_entidades"]
            form = forms.EntidadeForm()
        else:
            messages.error(request, "CORRIJA OS ERROS DO FORMULÁRIO ")
    else:
        form = forms.EntidadeForm()

    return render(
        request,
        "destinations/pages/entidades.html",
        context={
            "form": form,
        },
    )


def saidas(request):  # View de rota para registro de destino de produtos
    return render(
        request,
        "destinations/pages/registro-saidas.html",
        context={"saidas": [makeSaida() for _ in range(30)]},
    )


def registrodestino(request):  # View de rota para registro de doação
    return render(request, "destinations/pages/registro-destino.html")


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, "destinations/pages/gerar-planilha.html")

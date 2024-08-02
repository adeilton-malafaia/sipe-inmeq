from django.contrib import messages
from django.shortcuts import render

from destinations.models import Entidade
from utils.destinations.factory import makeSaida

from . import forms


def home(request):
    return render(request, "destinations/pages/index.html")


def entidades_insert(request):  # View de rota para cadastro de entidades
    if request.POST:
        POST = request.POST
        request.session["insert_form_entidades"] = POST
        form = forms.EntidadeForm(POST)
        ent = Entidade.objects.filter(cnpj=POST['cnpj'])
        if form.is_valid() and not ent:
            form.save(commit=True)
            messages.success(request, "ENTIDADE SALVA COM SUCESSO")
            del request.session["insert_form_entidades"]
            form = forms.EntidadeForm()
        else:
            messages.error(request, "CORRIJA OS ERROS DO FORMULÁRIO ")
    else:
        form = forms.EntidadeForm()

    return render(
        request,
        "destinations/pages/entidades-insert.html",
        context={
            "form": form,
        },
    )


def entidades_update(request):  # View da rota para update de entidades
    form = forms.EntidadeUpdateForm()
    if request.POST:
        POST = request.POST
        request.session["update_form_entidades"] = POST
        opt = dict(POST)['option'][0]
        id_value = dict(POST)['entidade'][0]

        match opt:
            case 'load':
                entidade = Entidade.objects.get(pk=id_value)
                form = forms.EntidadeUpdateForm(POST, instance=entidade)
            case 'save':
                if form.is_valid():
                    form.save(commit=True)
                    messages.success(request, "ENTIDADE SALVA COM SUCESSO")
                    del request.session["register_form_entidades"]
                    form = forms.EntidadeForm()
                else:
                    messages.error(request, "CORRIJA OS ERROS DO FORMULÁRIO ")

    return render(
        request,
        "destinations/pages/entidades-update.html",
        context={
            "form": form,
        },
    )


def saidas(request):  # View de rota para registro de saídas de produtos
    return render(
        request,
        "destinations/pages/registro-saidas.html",
        context={"saidas": [makeSaida() for _ in range(19)]},
    )


def registrodestino(request):  # View de rota para registro de doação
    return render(request, "destinations/pages/registro-destino.html")


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, "destinations/pages/gerar-planilha.html")

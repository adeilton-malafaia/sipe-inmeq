from django.contrib import messages
from django.shortcuts import render

from utils.destinations.factory import makeSaida

from . import forms, models


def home(request):
    return render(request, "destinations/pages/index.html")


def entidades_insert(request):  # View de rota para cadastro de entidades
    if request.POST:
        POST = request.POST
        request.session["insert_form_entidades"] = POST
        form = forms.EntidadeForm(POST)
        ent = models.Entidade.objects.filter(cnpj=dict(POST)['cnpj'][0])
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
    form = forms.EntidadeForm()
    options = models.Entidade.objects.filter(ativo='s')
    id_selected = None

    if request.POST:
        POST = request.POST
        request.session["update_form_entidades"] = POST
        option_match = dict(POST)['option'][0]
        id_selected = dict(POST)['selectEntidade'][0]

        match option_match:
            case 'load':
                entidade = models.Entidade.objects.get(pk=id_selected)
                form = forms.EntidadeForm(instance=entidade)

            case 'save':
                if form.is_valid():
                    form.save(commit=True)
                    messages.success(request, "ENTIDADE SALVA COM SUCESSO")
                    del request.session["update_form_entidades"]
                    form = forms.EntidadeForm()
                else:
                    messages.error(request, "CORRIJA OS ERROS DO FORMULÁRIO ")

    return render(
        request,
        "destinations/pages/entidades-update.html",
        context={
            "form": form,
            'options': options,
            'id_selected': id_selected
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

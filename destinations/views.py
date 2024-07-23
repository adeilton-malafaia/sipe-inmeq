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
        ent = models.Entidade.objects.filter(cnpj=POST['cnpj'])
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


def entidades_update(request):
    form = forms.EntidadeUpdateForm()
    if request.POST:
        POST = request.POST
        request.session["update_form_entidades"] = POST

        match POST['option']:
            case 'load':
                cnpj_value = POST['cnpj']
                ent = models.Entidade.objects.filter(cnpj=cnpj_value)
                form = forms.EntidadeUpdateForm(request.POST)
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


def saidas(request):  # View de rota para registro de destino de produtos
    return render(
        request,
        "destinations/pages/registro-saidas.html",
        context={"saidas": [makeSaida() for _ in range(19)]},
    )


def registrodestino(request):  # View de rota para registro de doação
    return render(request, "destinations/pages/registro-destino.html")


def planilha(request):  # View de rota para planilha de produtos p/ doação
    return render(request, "destinations/pages/gerar-planilha.html")

"""
URL configuration for sipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def cadastro_entidades(request):
    return HttpResponse('Página de cadastro de entidades (app)')


def gerar_planilha(request):
    return HttpResponse('Página para gerar planilha (app)')


def registro_destino(response):
    return HttpResponse('Página para registrar destino (app)')


def registro_doacao(request):
    return HttpResponse('Página para registro de doação (app)')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastroentidade/', cadastro_entidades),
    path('gerarplanilha/', gerar_planilha),
    path('registrodestino/', registro_destino),
    path('registrodoacao/', registro_doacao)
]
